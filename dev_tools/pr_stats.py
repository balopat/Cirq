import dataclasses
import datetime
from typing import Optional, Tuple, List

import os
import sys
from github import Github

GITHUB_REPO_NAME = 'cirq'
GITHUB_REPO_ORGANIZATION = 'quantumlib'
ACCESS_TOKEN_ENV_VARIABLE = 'CIRQ_BOT_GITHUB_ACCESS_TOKEN'

_last_print_was_tick = False


def log(*args):
    global _last_print_was_tick
    if _last_print_was_tick:
        print()
    _last_print_was_tick = False
    print(*args)


@dataclasses.dataclass()
class PRInfo():
    number: int
    created_at: datetime.datetime
    closed_at: Optional[datetime.datetime]
    first_review_at: Optional[datetime.datetime]
    state: str

    def lifetime(self):
        return self._val_or_today(self.closed_at) - self.created_at

    def _val_or_today(self, val):
        if not val:
            return datetime.datetime.today()
        else:
            return val

    def time_in_review(self):
        if not self.first_review_at:
            return None
        return self._val_or_today(self.closed_at) - self.first_review_at

    def time_unreviewed(self):
        if not self.first_review_at and self.state == "closed":
            return self.lifetime()
        return self._val_or_today(self.first_review_at) - self.created_at

    def __repr__(self):
        return ";".join([
            repr(x) for x in [
                self.number, self.created_at,
                self.time_unreviewed(),
                self.time_in_review(),
                self.lifetime(), self.state
            ]
        ])


def my_repr(pr):
    first_review_at = None
    reviews = pr.get_reviews()
    if reviews.totalCount > 0:
        first_review_at = min([
            rev.submitted_at for rev in reviews if rev.submitted_at is not None
        ])
    return PRInfo(number=pr.number,
                  created_at=pr.created_at,
                  closed_at=pr.closed_at,
                  first_review_at=first_review_at,
                  state=pr.state)


def main():
    access_token = os.getenv(ACCESS_TOKEN_ENV_VARIABLE)
    if not access_token:
        print('{} not set.'.format(ACCESS_TOKEN_ENV_VARIABLE), file=sys.stderr)
        sys.exit(1)
    g = Github(access_token)
    repo = g.get_repo(f"{GITHUB_REPO_ORGANIZATION}/{GITHUB_REPO_NAME}")
    with open('all_prs.csv', newline='', mode="w") as f:
        pulls = repo.get_pulls(state='all')
        print(f"catching up to {pulls.totalCount}")
        for i in range(pulls.totalCount):
            print(f"{i};{my_repr(pulls[i])}")
            f.write(f"{i};{my_repr(pulls[i])}\n")


if __name__ == '__main__':
    main()

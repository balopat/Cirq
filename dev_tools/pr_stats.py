import dataclasses
import datetime
from typing import Optional

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
        return self._val_or_today(self.first_review_at) - self.created_at

    def __repr__(self):
        return f"{(self.number, self.created_at, self.time_unreviewed(), self.time_in_review(), self.lifetime(), self.state)}"

def repr(pr):
    first_review_at = None
    reviews = pr.get_reviews()
    if reviews.totalCount > 0:
        first_review_at = min([rev.submitted_at for rev in reviews])
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
    with open('prs3.csv', newline='',mode="w") as f:
        pulls = repo.get_pulls(state='all')
        for i in range(2044, 2045):
            print(f"{i};{repr(pulls[i])}")
            f.write(f"{i};{repr(pulls[i])}\n")

    # with open('prs.csv', newline='',mode="r") as csvfile:
    #     reader = csv.reader(csvfile, delimiter='\t')
    #     for row in reader:
    #         try:
    #             repo.get_label(row[0])
    #             print(f"skip: {row[0]}")
    #         except:
    #             print(f"create: {row}")
    #             repo.create_label(name=row[0],color=row[1],description=row[2])


if __name__ == '__main__':
    main()

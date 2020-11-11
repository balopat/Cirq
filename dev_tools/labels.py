import datetime
import traceback
from typing import Optional, List, Any, Dict, Set, Union

import json
import os
import time
import sys
from github import Github
import csv

from dev_tools.github_repository import GithubRepository

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


def main():
    access_token = os.getenv(ACCESS_TOKEN_ENV_VARIABLE)
    if not access_token:
        print('{} not set.'.format(ACCESS_TOKEN_ENV_VARIABLE), file=sys.stderr)
        sys.exit(1)
    g = Github(access_token)
    repo = g.get_repo(f"{GITHUB_REPO_ORGANIZATION}/{GITHUB_REPO_NAME}")
    # with open('labels.csv', newline='',mode="w") as csvfile:
    #     writer = csv.writer(csvfile, delimiter='|', quotechar='"')
    #     for l in repo.get_labels():
    #         writer.writerow([l.name, l.color,l.description])

    with open('labels.csv', newline='', mode="r") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            try:
                repo.get_label(row[0])
                print(f"skip: {row[0]}")
            except:
                print(f"create: {row}")
                repo.create_label(name=row[0], color=row[1], description=row[2])


if __name__ == '__main__':
    main()

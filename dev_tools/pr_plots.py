import csv

from dev_tools.pr_stats import PRInfo
import pandas as pd
from pandas import DataFrame
import datetime


def main():
    df = DataFrame()

    ## 3301;datetime.datetime(2020, 9, 7, 14, 4, 4);datetime.timedelta(seconds=9072);datetime.timedelta(seconds=75585);datetime.timedelta(seconds=84657);closed
    headers = [("id", int), ("created_at", eval), ("time_unreviewed", eval),
               ("time_in_review", eval), ("lifetime", eval), ("state", str)]
    with open('all_prs.csv', newline='', mode="r") as f:
        for row in f:
            cols = row.split(";")
            df = df.append(
                {
                    headers[i][0]: headers[i][1](cols[i])
                    for i in range(len(headers))
                },
                ignore_index=True)

    print(df)


if __name__ == '__main__':
    main()

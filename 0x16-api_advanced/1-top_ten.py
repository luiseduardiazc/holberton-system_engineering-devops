#!/usr/bin/python3
"""Queries the Reddit API"""
import requests


def top_ten(subreddit):
    """returns first 10 posts from Reddit API"""

    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    header = {"User-Agent": "Test"}
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        for item in r.json().get("data", None).get("children", None):
            print(item.get("data", None).get("title", None))
    else:
        print(None)


if __name__ == "__main__":
    top_ten('programing')

#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns total"""
    header = {"User-Agent": "Test"}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        return r.json().get("data", None).get("subscribers", None)
    else:
        return 0

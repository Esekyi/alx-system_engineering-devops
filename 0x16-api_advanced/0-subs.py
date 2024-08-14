#!/usr/bin/python3
"""accessing all subscribers from reddit api"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    Main function
    make a aget request to redit api to get subscribers
    """

    # subreddit = argv[1]
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

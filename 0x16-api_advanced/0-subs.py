#!/usr/bin/python3
import requests
from sys import argv


def number_of_subscribers(subreddit):
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

if __name__ == "__main__":
    number_of_subscribers(argv[1])
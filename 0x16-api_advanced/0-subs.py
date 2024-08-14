#!/usr/bin/python3
"""accessing all subscribers from reddit api"""
import requests


def number_of_subscribers(subreddit):
    """
    Main function
    make a aget request to redit api to get subscribers
    """
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except requests.RequestException as e:
        return 0

#!/usr/bin/python3
"""accessing all first 10 posts from redit"""
import requests


def top_ten(subreddit):
    """
    Main function
    make a aget request to redit api to get subscribers
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            for post in data:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException as e:
        print(None)

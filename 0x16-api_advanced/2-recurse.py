#!/usr/bin/python3
"""a recursive script """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Main function -
    Recursively retrives a list of titles from
    all post (hot posts) on reddit
    """

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {
        'after': after,
        'limit': 100,
    }
    try:
        response = requests.get(
            url, params=params, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            for post in children:
                hot_list.append(post['data']['title'])
            after = data.get('after', None)
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException as e:
        return None

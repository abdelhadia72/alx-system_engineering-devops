#!/usr/bin/python3
""" Top 10 subscribers """
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/subreddits/popular.json"
    response = requests.get(url, headers={})

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            if len(posts) == 0:
                print("No posts found in this subreddit.")
            else:
                print("Top 10 posts in", subreddit, ":")
                for post in posts[:10]:
                    print(post['data']['title'])
        else:
            print("No data found for this subreddit.")
    else:
        print("Failed to fetch data.")

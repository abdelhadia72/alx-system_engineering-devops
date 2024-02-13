#!/usr/bin/python3
""" Top hot articles """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
        Recurse function
    """
    req = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if req.status_code == 200:
        data = req.json().get("data")
        if data and "children" in data:
            for child in data["children"]:
                if "data" in child and "title" in child["data"]:
                    hot_list.append(child["data"]["title"])
            after = data.get("after")
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None

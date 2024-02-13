#!/usr/bin/python3
""" Module for storing the count_words function. """
from requests import get


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Prints the count of the given words present in the title of the
    subreddit's hottest articles.
    """
    if word_count is None:
        word_count = {}

    headers = {'User-Agent': 'Firefox/102.0'}

    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    r = get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return

    data = r.json().get('data')
    if not data:
        return

    children = data.get('children', [])
    for child in children:
        title_words = set(child['data']['title'].lower().split())
        for word in word_list:
            if word.lower() in title_words:
                word_count[word] = word_count.get(word, 0) + 1

    after = data.get('after')
    if after:
        count_words(subreddit, word_list, word_count, after)
    else:
        sorted_words = sorted(word_count.items(),
                              key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f'{word}: {count * word_list.count(word)}')

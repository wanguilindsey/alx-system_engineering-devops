#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count of
given keywords (case-insensitive, delimited by spaces.
"""

import requests


def count_words(subreddit, word_list, after=None, word_counts={}):
    """recursive function that queries the Reddit API, parses the
    title of all hot articles, and prints a sorted count of
    given keywords (case-insensitive, delimited by spaces."""

    base_url = 'https://www.reddit.com/r/'
    url = f"{base_url}{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        if not children:
            sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1],
                                                                       x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return
        for child in children:
            title = child['data']['title'].lower()
            for word in word_list:
                if word.lower() in title.split():
                    if word.lower() in word_counts:
                        word_counts[word.lower()] += 1
                    else:
                        word_counts[word.lower()] = 1
        after = data['data']['after']
        return count_words(subreddit, word_list, after, word_counts)
    else:
        return


if __name__ == '__main__':
    subreddit = 'programming'
    word_list = ['react', 'python', 'java', 'javascript',
                 'scala', 'no_results_for_this_one']
    count_words(subreddit, word_list)

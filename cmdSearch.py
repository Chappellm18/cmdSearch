#!/usr/bin/env python3

import webbrowser
import sys

search_pages = [
    'stackoverflow.com',
    'github.com',
    'youtube.com',
    'medium.com',
]

url = "https://www.google.com/search?q="
firefox_path = "C:/Program Files/Firefox Developer Edition/firefox.exe"


def create_url():
    query = sys.argv[1:]
    return ' '.join(query)


def filter_searchs():
    filter_str = '('
    for index, website in enumerate(search_pages):
        filter_str += 'site:' + website
        if index == len(search_pages) - 1:
            filter_str += ')'
        else:
            filter_str += ' OR '
    return filter_str


if __name__ == '__main__':
    if len(sys.argv[1:]) == 0:
        print('No search query')
    else:
        final_url = url + create_url() + filter_searchs()
        webbrowser.Mozilla(firefox_path).open(final_url)

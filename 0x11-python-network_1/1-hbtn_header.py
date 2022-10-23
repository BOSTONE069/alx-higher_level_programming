#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id
"""
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) \
            as response:
        print(dict(response.headers).get("X-Request-Id"))

#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id
"""
import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(dict(r.headers).get("X-Request-Id"))

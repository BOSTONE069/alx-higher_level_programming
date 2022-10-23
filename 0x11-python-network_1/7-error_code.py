#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    request = requests.get(url)
    if request.status_code >= 400:
        print(f"Error code: {request.status_code}")
    else:
        print(request.text)

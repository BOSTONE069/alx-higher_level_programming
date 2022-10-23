#!/usr/bin/python3
"""script that takes in a URL and an email,
sends a POST request to the passed
URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    values = {"email": sys.argv[2]}

    request = requests.post(url, data=values)
    print(request.text)

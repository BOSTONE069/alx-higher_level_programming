#!/usr/bin/python3
"""python script for fetching data in url"""
import requests

if __name__ == '__main__':
    request = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"type: {request.text}")
    print(f"content: {request.text}")

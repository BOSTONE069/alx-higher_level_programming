#!/usr/bin/python3
"""script that takes in a letter and
sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) != 2:
        print("No result")
    else:
        letter = sys.argv[1]
        if letter:
            data = {'q': sys.argv[1]}
        else:
            data = {'q': ''}
        response = requests.post(url, data)
        try:
            json_response = response.json()
            if not json_response.get('id'):
                print("No result")
            else:
                print(f"[{json_response.get('id')}] {json_response.get('name')}")
        except:
            print("Not a valid JSON")

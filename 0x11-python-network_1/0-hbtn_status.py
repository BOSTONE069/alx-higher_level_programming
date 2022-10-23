#!/usr/bin/python3
"""python script for fetching data in url"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        alx = response.read()

        print('Body response:')
        print(f'\t- type: {type(alx)}')
        print(f'\t- content-type: {alx}')
        print(f'\t- utf8 content: {alx.decode("utf-8", "replace")}')


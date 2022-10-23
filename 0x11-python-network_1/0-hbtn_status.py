#!/usr/bin/python3
"""python script for fetching data in url"""

if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        alx = response.read()

        print('Body response:')
        print('\t- type: {}'.format(type(alx)))
        print('\t- content-type: {}'.format(alx))
        print('\t- utf8 content: {}'.format(alx.decode("utf-8", "replace")))

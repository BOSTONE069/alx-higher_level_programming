#!/usr/bin/python3
"""python script for fetching data in url"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        alx = response.read()

        print('Body response:')
        print('\t- type: {}'.format(type(alx)))
        print('\t- content-type: {}'.format(alx))
        print('\t- utf8 content: {}'.format(alx.decode("utf-8", "replace")))

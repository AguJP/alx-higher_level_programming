#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')as response:
        status = response.read()
        print("Body response:")
        print("    - type: {}".format(type(status)))
        print("    - content: {}".format(status))
        print("    - utf8 content: {}".format(status.decode('utf-8')))

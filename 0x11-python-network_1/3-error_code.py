#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
- displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.error

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

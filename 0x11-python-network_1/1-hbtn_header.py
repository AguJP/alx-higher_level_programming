#!/usr/bin/python3
"""This script:
-Takes a URL
-Sends a request to the URL
-Displays the value of `X-Request-Id` variable of the header
"""


if __name__ == '__main__':
    import urllib.request
    import sys
    
    url = sys.argv[1]
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))

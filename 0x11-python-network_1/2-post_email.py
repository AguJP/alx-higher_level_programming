#!/usr/bin/bash
"""script that takes in a URL and an email,
- sends a POST request to the passed URL with the email as a parameter,
-  and displays the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    import urllib.request
    import sys
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    email = urllib.parse.urlencode(email)
    email = email.encode('utf-8')
    
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))

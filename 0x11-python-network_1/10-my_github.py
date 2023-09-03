#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
- Uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    url = 'https://api.github.com/user'
    authenticate = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    req = requests.get(url, authenticate)
    print(req.json().get("id"))

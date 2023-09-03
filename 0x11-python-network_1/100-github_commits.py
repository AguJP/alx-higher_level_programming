#!/usr/bin/python3
"""list 10 commits (from most recent) of the repo “rails” by user “rails”
- Print all commits by: `<sha>: <author name>` (one by line)
- argv[1] = repository name, argv[2] = owner name
"""


if __name__ == "__main__":
    import requests
    import sys


    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try:
        for j in range(10):
            print("{}: {}".format(commits[j].get("sha"), commits[j].get(
                "commit").get("author").get("name")))
    except IndexError:
        pass

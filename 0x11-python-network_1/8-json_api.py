#!/usr/bin/python3
"""script that takes in a letter
- Sends a POST request to http://0.0.0.0:5000/search_user
- with the letter as a parameter
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    q = {"q": letter}

    try:
        req = requests.post(url, q)
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

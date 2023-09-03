#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    request = requests.get('https://alx-intranet.hbtn.io/status')
    disp = request.text
    
    print("Body response:")
    print("\t- type: {}".format(type(disp)))
    print("\t- content: {}".format(disp))

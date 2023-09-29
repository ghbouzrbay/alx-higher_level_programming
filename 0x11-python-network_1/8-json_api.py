#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the body of the response"""

import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        d = sys.argv[1]
    else:
        d = ""
    payload = {"q": d}
    response = requests.post(url, data=payload)
    try:
        json_output = response.json()
        if not json_output:
            print("No result")
        else:
            idd = json_output.get("id")
            name = json_output.get("name")
            print("[{}] {}".format(idd, name))
    except ValueError as invalid_json:
        print("Not a valid JSON")

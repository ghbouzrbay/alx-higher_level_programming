#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the body of the response"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    response = requests.post("http://0.0.0.0:5000/search_user",
                             data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"),
                                   response.get("name")))
    except ValueError:
        print("Not a valid JSON")

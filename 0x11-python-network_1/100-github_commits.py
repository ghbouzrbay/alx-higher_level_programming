#!/usr/bin/python3
"""
script that takes 2 arguments in order to list 10 commits (from the most
recent to oldest) of the repository "rails" by the user "rails".
"""

import sys
import requests


if __name__ == "__main__":
    try:
        repository_name = sys.argv[1]
        username = sys.argv[2]
        url = "https://api.github.com/repos/{}/{}/commits" \
            .format(username, repository_name)
        response = requests.get(url)
        fjson = response.json()
        for i, objct in enumerate(fjson):
            if i == 10:
                break
            if type(objct) is dict:
                name = objct.get('commit').get('author').get('name')
                print("{}: {}".format(objct.get('sha'), name))
    except ValueError as invalid_json:
        pass

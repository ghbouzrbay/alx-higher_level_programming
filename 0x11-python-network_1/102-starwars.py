#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars API."""

import sys
import requests


if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    par = {"search": sys.argv[1]}
    response = requests.get(url, par=par).json()

    count = response.get("count")
    print("Number of results: {}".format(response.get("count")))

    i = 0
    while i < count:
        for result in response.get("results"):
            print(result.get("name"))
            for lien in result.get("films"):
                mv = requests.get(lien).json()
                print("\t{}".format(mv.get("title")))
            i += 1

        page = response.get("next")
        if page is not None:
            response = requests.get(page).json()

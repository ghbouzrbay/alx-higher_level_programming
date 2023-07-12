#!/usr/bin/python3

""" function that writes an Object to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation

    Args:
        my_obj (obj): any object for example list, dict
        filename: file name
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

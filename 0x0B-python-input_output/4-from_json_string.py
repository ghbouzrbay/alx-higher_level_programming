#!/usr/bin/python3

""" function that returns an object (Python data structure) represented by a JSON string"""

import json


def from_json_string(my_str):
    """from_json_string  returns the Python object represented by a JSON string

    Args:
        my_str (obj): any object for example list, dict
    """
    return (json.loads(my_str))

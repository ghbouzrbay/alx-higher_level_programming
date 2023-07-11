#!/usr/bin/python3

def class_to_json(obj):
    """class_to_json return dictionary description with simple data structure

    Args:
        obj : any object for example list, dict
    """
    return obj.__dict__

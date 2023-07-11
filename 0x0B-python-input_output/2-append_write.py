#!/usr/bin/python3

"""function that appends a string at the end of a text file (UTF8) and returns the number of characters added"""

def append_write(filename="", text=""):
    """append_write appends a string at the end of a text file (UTF8)

    Args:
        filename (str): Defaults to "".
        text (str): text to add. Defaults to "".
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

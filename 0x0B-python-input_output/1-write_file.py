#!/usr/bin/python3

def write_file(filename="", text=""):
    """write_file writes a string to a text file  (UTF8)

    Args:
        filename (str): Defaults to "".
        text (str): text to add. Defaults to "".
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

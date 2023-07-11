#!/usr/bin/python3

"""function that writes a string to a text file (UTF8) and returns the number of characters written"""

def number_of_lines(filename=""):
    """number_of_lines: returns the number of lines of a text file:

    Args:
        filename (str): content of the file. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return len(f.readlines())

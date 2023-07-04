#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        words = (delimeter + "\n\n").join(
                [index.strip(" ") for index in words.split(delimeter)])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

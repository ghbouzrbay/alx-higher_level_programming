#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""

def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.
    Args:
        list_of_integers (list): a list of integers
    Returns:
        int: peak(s)
    """
    int_list = list_of_integers
    if int_list == []:
        return None
    length = len(int_list)

    start, end = 0, length - 1
    while start < end:
        middel = start + (end - start) // 2
        if (int_list[middel] > int_list[middel - 1] and
            int_list[middel] > int_list[middel + 1]):
            return int_list[middel]
        if int_list[middel - 1] > int_list[middel + 1]:
            end = middel
        else:
            start = middel + 1
    return int_list[start]

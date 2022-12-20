#!/usr/bin/python3
"""
This module contains a single function
 to find the peak from a list of integers
"""


def find_peak_r(arr, start, end):

    """Recursively find the pick of an array
    Args:
        arr: List of integers
        start: starting index
        end: ending index
    """

    if start == end:
        return start
    elif (start + 1) == end:
        if arr[start] > arr[end]:
            return start
        return end
    else:
        mid = (start + end) // 2
        if (arr[mid] > arr[mid - 1]) and (arr[mid] > arr[mid + 1]):
            return mid
        elif (arr[mid - 1] > arr[mid]) and (arr[mid] > arr[mid + 1]):
            return find_peak_r(arr, start, mid - 1)
        else:
            return find_peak_r(num, mid + 1, end)


def find_peak(list_of_integers):
    """Finds the peak from a list of intgers
    Args:
            list_of_integers: Well, the name explains itself

    Returns: The peak integer from the list
    """
    return find_peak_r(list_of_integers, 0, len(list_of_integers))

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

    mid = (start + end) // 2

    if (mid == 0 or arr[mid - 1] <= arr[mid]) and
    (mid == (n - 1) or arr[m + 1] <= arr[mid]):
        return mid

    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return find_peak_r(arr, start, mid - 1)

    else:
        return find_peak_r(arr, mid + 1, end)


def find_peak(list_of_integers):
    """Finds the peak from a list of intgers
    Args:
            list_of_integers: Well, the name explains itself

    Returns: The peak integer from the list
    """
    peak_index = find_peak_r(list_of_integers, 0, len(list_of_integers))

    return list_of_integers[peak_index]

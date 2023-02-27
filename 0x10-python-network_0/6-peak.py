#!/usr/bin/python3
"""
This module contains a single function
 to find the peak from a list of integers
"""


def find_peak(list_of_integers):
    """Finds the peak from a list of intgers
    Args:
            list_of_integers: Well, the name explains itself

    Returns: The peak integer from the list
    """

    n = len(list_of_integers)

    end = n
    mid = n // 2

    if n == 0:
        return None

    while True:
        end = end // 2

        if (mid < n - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if end // 2 == 0:
                end = 2
            mid = mid + end // 2

        elif end > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if end // 2 == 0:
                end = 2
        else:
            return list_of_integers[mid]

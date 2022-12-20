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
    if len(list_of_integer) == 0:
        return None

    peak = list_of_integers[0]

    for integer in list_of_integer:
        if integer > peak:
            peak = integer

    return peak

#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list

    Args:
        my_list: List of integers

    Returns:
        Sum of unique elements
    """
    return sum(set(my_list))

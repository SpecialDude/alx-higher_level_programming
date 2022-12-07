#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2

    Args:
        my_list: List of Integers

    Returns:
        Lists
    """

    return [num % 2 == 0 for num in my_list]

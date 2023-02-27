#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print a List in reverse

    Args:
        my_list: List of integers to print

    Returns:
        None
    """
    if not my_list:
        return

    for i in range(len(my_list) - 1, -1, -1):
        print(str.format("{:d}", my_list[i]))

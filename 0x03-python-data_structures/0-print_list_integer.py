#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print List of integer

    Args:
        my_list: List of integers

    Returns:
        None
    """

    for i in range(len(my_list)):
        print(str.format("{:d}", my_list[i]))

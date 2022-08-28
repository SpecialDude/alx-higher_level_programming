#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Make a copy of list and replaces element at id

    Args:
        my_list: List of integers
        idx: index
        element: Integer element to replace with

    Returns:
        Copied list
    """

    copy_list = my_list[:]

    if not (idx < 0 or idx >= len(my_list)):
        copy_list[idx] = element

    return (copy_list)

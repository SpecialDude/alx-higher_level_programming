#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element in a list

    Args:
        my_list: List of Integer
        idx: Element position
        element: Integer

    Returns:
        my_list if idx in out of range else None
    """

    if idx < 0 or idx >= len(my_list):
        return (my_list)

    my_list[idx] = element
    return (my_list)

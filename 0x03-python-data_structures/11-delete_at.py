#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete element at index idx in my_list

    Args:
        my_list: List of Integers
        idx: element idx

    Returns:
        my_list
    """

    if idx < 0 or idx >= len(my_list):
        return (my_list)

    del my_list[idx]
    return (my_list)

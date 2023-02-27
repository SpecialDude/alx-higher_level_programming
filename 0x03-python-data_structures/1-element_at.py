#!/usr/bin/python3
def element_at(my_list, idx):
    """Get element at idx in my_list

    Args:
        my_list: List
        idx: Index

    Returns:
       Integer
    """

    if idx < 0 or idx >= len(my_list):
        return (None)

    return (my_list[idx])

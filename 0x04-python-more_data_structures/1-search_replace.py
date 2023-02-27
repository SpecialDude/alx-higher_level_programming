#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Search and Replaces an Element in a list

    Args:
        my_list: List of integers
        search: Element to search for
        replace: Element to replace with

    Returns:
        New list
    """

    return list(map(lambda x: replace if x == search else x, my_list))

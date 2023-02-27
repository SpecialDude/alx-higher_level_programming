#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a_dictionary.

    Args:
        a_dictionary: Dictionary

    Returns:
        None
    """
    a_dictionary.update({key: value})

    return a_dictionary

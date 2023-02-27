#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary: A Dictionary
        value: A value in dictionary

    Returns:
        Modified dictionary
    """
    keys = list(
        filter(lambda x: a_dictionary[x] == value, a_dictionary.keys())
    )

    for key in keys:
        del a_dictionary[key]

    return a_dictionary

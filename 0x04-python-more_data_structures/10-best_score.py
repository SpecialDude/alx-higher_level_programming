#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value

    Args:
        a_dictionary: Dictionary

    Returns:
        Key
    """

    if not a_dictionary:
        return None

    enum = list(a_dictionary.items())
    max_k, max_value = enum[0]

    for key, value in enum[1:]:
        if value > max_value:
            max_k, max_value = key, value
    return max_k

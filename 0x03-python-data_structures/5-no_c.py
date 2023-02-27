#!/usr/bin/python3
def no_c(my_string):
    """Replaces all 'c' and 'C' in my_string

    Args:
        my_string: String to replace in

    Returns:
        The new replaced string
    """

    new_str = ""
    for c in my_string:
        if not (c == 'C' or c == 'c'):
            new_str += c

    return (new_str)

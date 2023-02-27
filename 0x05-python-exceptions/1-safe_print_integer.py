#!/usr/bin/python3

def safe_print_integer(value):
    """Safely Print an integer value

    Args:
        value: an integer

    Return:
        Bool
    """

    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False

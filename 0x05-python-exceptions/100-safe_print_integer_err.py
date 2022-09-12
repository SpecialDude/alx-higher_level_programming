#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Safely Print an integer value

    Args:
        value: an integer

    Return:
        Bool
    """

    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False

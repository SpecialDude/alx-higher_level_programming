#!/usr/bin/python3

def safe_print_integer(value):
    """Safely Print an integer value

    Args:
        value: an integer

    Return:
        Boil
    """

    try:
        print("{:d}".format(value))
        return True
    except:
        return False

#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Safely Print an integer value

    Args:
        fct: function pointer
        args: Arguments

    Return:
        function returned value or None on error
    """

    try:
        return fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None

#!/usr/bin/python3

""""
Well, another module that contains some
function: is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class

    Args:
        obj: any object instance
        a_class: any class

    Returns:
        Boolean value
    """

    return isinstance(obj, a_class)

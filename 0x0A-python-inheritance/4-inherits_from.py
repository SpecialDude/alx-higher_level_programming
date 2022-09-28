#!/usr/bin/python3

""""
Well, another module that contains some
function: inherits_from
"""


def inherits_from(obj, a_class):
    """Checks if obj is a subclass of a_class

    Args:
        obj: any object instance
        a_class: any class

    Returns:
        Boolean value
    """

    return issubclass(type(obj), a_class)

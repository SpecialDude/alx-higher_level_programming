#!/usr/bin/python3

""""
Seriously I'm tired of writing module docs

Well, another module that contains some
sh** function: is_same_class
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

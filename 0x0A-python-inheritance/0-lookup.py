#!/usr/bin/python3

"""
Some function to lookup an object's attributes
"""


def lookup(obj):
    """Returns an object's attributes and method

    Args:
        obj: a python object

    Returns:
        a list object containing obj's attributes
    """

    return dir(obj)

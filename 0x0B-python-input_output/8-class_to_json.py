#!/usr/bin/python3

"""
This module contains a single function to return
a class's attributes

class_to_json()
"""


def class_to_json(obj):
    """Returns all attributes of an object as a dictionary

    Args:
        obj: A python object
        filename: str

    Returns:
        dict
    """

    return obj.__dict__

#!/usr/bin/python3

"""
Defines a function that adds atributes
to a class
"""


def add_attribute(instance, name, value):
    """Add attribute to instance of a class"""

    if not hasattr(instance, name) and not hasattr(instance, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(instance, name, value)

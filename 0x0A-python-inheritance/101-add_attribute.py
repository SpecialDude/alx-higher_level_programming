#!/usr/bin/python3

"""
Defines a function that adds atributes
to a class
"""


def add_attribute(instance, name, value):
    """Add attribute to instance of a class"""

    if hasattr(instance, '__dict__'):
        setattr(instance, name, value)

    if hasattr(instance, '__slot__'):
        raise TypeError("can't add new attribute")

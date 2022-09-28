#!/usr/bin/python3

"""
Defines a function that adds atributes
to a class
"""


def add_attribute(instance:object, name, value):
    """Add attribute to instance of a class"""

    if not hasattr(instance, '__slot__'):
        setattr(instance, name, value)

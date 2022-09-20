#!/usr/bin/python3

"""
A Locked Class
You cannot dynamically create new instace attributes
"""


class LockedClass:
    """A locked class allowing only one attributes"""

    __slots__ = ['first_name']

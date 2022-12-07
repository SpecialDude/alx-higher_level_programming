#!/usr/bin/python3

"""
A base class definition
"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """To be implemented by the inheriting classes"""

        raise Exception("area() is not implemented")

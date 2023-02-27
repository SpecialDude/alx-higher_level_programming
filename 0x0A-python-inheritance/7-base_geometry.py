#!/usr/bin/python3

"""
A base class definition
"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """To be implemented by the inheriting classes"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))

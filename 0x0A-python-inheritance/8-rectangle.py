#!/usr/bin/python3


"""
Defines a Rectangle class Extending
the BaseGeometry Class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class subclassing BaseGeometry"""

    def __init__(self, width, height):
        """Instance initialization

        Args:
            width: width of Rectangle (int)
            height: height of Rectangle (int)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

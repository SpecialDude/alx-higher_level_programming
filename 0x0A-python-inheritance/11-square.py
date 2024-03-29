#!/usr/bin/python3


"""
Defines a Square class Extending
the Rectangle Class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class subclassing Rectangle class"""

    def __init__(self, size):
        """Instance initialization

        Args:
            size: size of Square (int)
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Returns area of square"""

        return self.__size ** 2

    def __str__(self):
        """String representation of class"""

        return "[Square] {}/{}".format(self.__size, self.__size)

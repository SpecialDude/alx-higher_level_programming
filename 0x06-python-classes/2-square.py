#!/usr/bin/python3

"""
I swear y'all are bunch of crazy people,
Yeah I said it (Crazy people)

"""


class Square:
    """Square class with one member variable."""
    def __init__(self, size=0):
        """Initializer

        Args:
            size: size - int

        Returns:
            None
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

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

        self.__validator(size)

        self.__size = size

    def area(self):
        """Returns the Area of square"""

        return (self.__size ** 2)

    def __validator(self, size):
        """Validator - Validates size

        Args:
            size: size - int

        Returns:
            None
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Returns the instance size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the instance size"""

        self.__validator(value)
        self.__size = value

    def __eq__(self, o_square):
        """Square area equality"""

        return self.area() == o_square.area()

    def __ne__(self, o_square):
        """Square area equality"""

        return self.area() != o_square.area()

    def __gt__(self, o_square):
        """Square area comparison"""

        return self.area() > o_square.area()

    def __lt__(self, o_square):
        """Square area comparison"""

        return self.area() < o_square.area()

    def __ge__(self, o_square):
        """Square area comparison"""

        return self.area() >= o_square.area()

    def __le__(self, o_square):
        """Square comparison"""

        return self.area() <= o_square.area()

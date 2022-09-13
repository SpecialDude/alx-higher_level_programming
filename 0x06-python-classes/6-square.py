#!/usr/bin/python3

"""
I swear y'all are bunch of crazy people,
Yeah I said it (Crazy people)

"""


class Square:
    """Square class with one member variable."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializer

        Args:
            size: size - int

        Returns:
            None
        """

        self.__validator(size, position)

        self.__size = size
        self.__position = position

    def area(self):
        """Returns the Area of square"""

        return (self.__size ** 2)

    def __validator(self, size=None, position=None):
        """Validator - Validates size

        Args:
            size: size - int

        Returns:
            None
        """
        if size:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")

        if position:
            if not isinstance(position, tuple) or \
                len(position) != 2 or \
                not isinstance(position[0], int) or \
                    not isinstance(position[1], int):
                raise TypeError(
                    "position must be a tuple of 2 positive integers"
                )

    @property
    def size(self):
        """Returns the instance size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the instance size"""

        self.__validator(size=value)
        self.__size = value

    @property
    def position(self):
        """Returns the instance position"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the instance position"""

        self.__validator(position=value)
        self.__size = value

    def my_print(self):
        """Prints a square with size"""

        if self.__size == 0:
            print()
            return
        c = ("_" * self.__position[0]) + "#"
        print(((c * self.__size) + "\n") * self.__size, end="")

#!/usr/bin/python3

"""
This module contains a Rectangle class
"""


class Rectangle:
    """A Rectangle class with few definitions"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialization Method"""

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Returns the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of triangle"""

        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of Rectangle"""

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """String Representation of class"""

        if self.width == 0 or self.height == 0:
            return ""

        row = ("{}".format(self.print_symbol)) * self.width

        rect = (row + "\n") * (self.height - 1)
        rect += row

        return rect

    def __repr__(self):
        """Official String Representation of class"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Greets goodbye when an instace is deleted"""

        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare Two Rectangle Objects"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1:
            return rect_2
        return rect_1

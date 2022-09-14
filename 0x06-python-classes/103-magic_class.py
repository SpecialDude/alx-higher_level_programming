#!/usr/bin/python3
"""I swear y'all are bunch of crazy people"""
import math


class MagicClass:
    """Some class Definition"""
    def __init__(self, radius):
        """Initialization of circle"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Area of circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Circumference of circle"""
        return 2 * math.pi * self.__radius

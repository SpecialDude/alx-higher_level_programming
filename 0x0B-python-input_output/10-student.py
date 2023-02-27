#!/usr/bin/python3

"""
Module contain a single class having
a method to return instances as json
"""


class Student:
    """
    A simple class with a method to return
    instaces as strings
    """
    def __init__(self, first_name, last_name, age):
        """Returns all attributes of an object as a dictionary

        Args:
            first_name: str
            last_name: str
            age: int
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns all attributes of instance as a dictionary

        Args:
            attrs: List of attributes desired to obtain

        Returns:
            dict
        """

        if isinstance(attrs, list):
            return {
                attr: self.__dict__[attr]
                for attr in attrs if attr in self.__dict__
            }

        return self.__dict__

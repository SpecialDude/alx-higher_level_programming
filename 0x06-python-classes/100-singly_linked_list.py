#!/usr/bin/python3

"""
I swear y'all are bunch of crazy people,
Yeah I said it (Crazy people)

"""


class Node:
    """A class representing a Linked list node."""

    def __init__(self, data, next_node=None):
        """Initializer

        Args:
            data: data
            next_node: Node

        Returns:
            None
        """

        self.__validator(data, next_node)

        self.__data = data
        self.__next_node = next_node

    def __validator(self, data=None, next_node=None):
        """Validator - Validates data and node

        Args:
            size: size - int

        Returns:
            None
        """
        if data:
            if not isinstance(data, int):
                raise TypeError("data must be an integer")

        if next_node:
            if not isinstance(next_node, Node):
                raise TypeError(
                    "next_node must be a Node object"
                )

    @property
    def data(self):
        """Returns the instance data"""

        return self.__data

    @data.setter
    def size(self, value):
        """Sets the instance data"""

        self.__validator(data=value)
        self.__data = value

    @property
    def next_node(self):
        """Returns the instance next_node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the instance next_node"""

        self.__validator(next_node=value)
        self.__next_node = value


class SinglyLinkedList:
    """A class representing a Singly Linked list."""

    def __init__(self):
        """Initializer

        Args:
            None

        Returns:
            None
        """

        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head == None:
            self.__head = new_node
            return

        if self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head

        while current and current.next_node:
            if current.next_node.data > value:
                break

            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """String representation of class"""

        current = self.__head
        rep = ''

        while current:
            rep += str.format('{:d}\n', current.data)
            current = current.next_node

        return rep

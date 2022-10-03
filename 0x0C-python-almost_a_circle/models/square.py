#!/usr/bin/python3

"""
Module contains a Square class subclassing
the rectangle class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A Square class subclassing rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instance Initialization"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of class"""

        return (
            "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width,
            )
        )

    @property
    def size(self):
        """Returns the size of instance Square"""

        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of instance Square"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update class attributes"""

        attrs = ['id', 'size', 'x', 'y']

        if args:
            for i in range(min((len(args), len(attrs)))):
                setattr(self, attrs[i], args[i])

        else:
            for attr, value in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, value)

    def to_dictionary(self):
        """Dictionary representation of instance attribute"""

        return {
            'size': self.size,
            'x': self.x,
            'y': self.y,
            'id': self.id
        }

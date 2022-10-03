#!/usr/bin/python3

"""
Some Rectangle class is defined here
"""


from models.base import Base


class Rectangle(Base):
    """A Rectangle class subclassing the Base class"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """Instance Instantiation
        Args:
            width: width of rectangle
            height: height of rectangle
            x: Position x
            y: Position y
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id=id)

    @property
    def width(self):
        """Returns the width of instance Rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of instance Rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 1:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Returns the height of instance Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of instance Rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 1:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Returns the x position of instance Rectangle"""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x position of instance Rectangle"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Returns the y position of instance Rectangle"""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y position of instance Rectangle"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Return the area of Rectangle"""

        return self.width * self.height

    def display(self):
        """Displays Rectangle at stdout with '#'"""

        y_pad = "\n" * self.y
        x_pad = " " * self.x

        row = x_pad + (("{}".format('#')) * self.width)

        rect = y_pad + ((row + "\n") * (self.height - 1))
        rect += row

        print(rect)

    def __str__(self):
        """String representation of class"""

        return (
            "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.x,
                self.y,
                self.width,
                self.height
            )
        )

    def __repr__(self):
        """String representation of class"""
        
        return self.__str__()

    def update(self, *args, **kwargs):
        """Update class attributes"""

        attrs = ['id', 'width', 'height', 'x', 'y']

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
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
            'id': self.id
        }


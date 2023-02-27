#!/usr/bin/python3

"""
Module Contains a Base class that will be
derived by some future model classes
"""

import json
import os
import turtle
import random
from models.numbersdraw import write_digits


class Base:
    """Model Base class, keeps id number of instances"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instance Initialization

        Args:
            id: integer
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list of dictionaries to json string"""

        if not list:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of object to file"""

        filename = cls.__name__ + ".json"

        with open(filename, 'w', encoding="UTF-8") as fd:
            if list_objs:
                fd.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Converts json string to list of dictionaries"""

        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new Instance fro dictionary"""

        instance = cls(1, 1, 1, 1)

        instance.update(**dictionary)

    @classmethod
    def load_from_file(cls):
        """load a list of object from file"""

        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []

        with open(filename, encoding="UTF-8", mode='r') as fd:

            data = json.load(fd)

        return [cls.from_json_string(js) for js in data]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of object to csv file"""

        filename = cls.__name__ + ".csv"

        if cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]
        else:
            fields = ["id", "width", "height", "x", "y"]

        with open(filename, 'w', encoding="UTF-8") as fd:
            fd.write(','.join(fields) + '\n')

            if list_objs:
                data = [
                    ",".join(
                        [str(getattr(obj, attr)) for attr in fields]
                    )
                    for obj in list_objs
                ]

                for row in data:
                    fd.write(row + '\n')

    @classmethod
    def load_from_file_csv(cls):
        """load a list of object from csv file"""

        filename = cls.__name__ + ".csv"

        if not os.path.exists(filename):
            return []

        with open(filename, encoding="UTF-8", mode='r') as fd:

            data = fd.readlines()

        objs = []

        if data:
            fields = data[0].rstrip('\n').split(',')

            for row in data[1:]:
                row = row.rstrip('\n').split(',')
                obj = cls(1, 1, 1, 1)
                obj.update(**{fields[i]: int(row[i]) for i in range(len(row))})
                objs.append((obj))

        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws shape using the turtle module"""

        def draw_rect(w, h, turtle):
            turtle.setheading(0)
            turtle.pendown()
            turtle.forward(w)
            turtle.rt(90)
            turtle.forward(h)
            turtle.rt(90)
            turtle.forward(w)
            turtle.rt(90)
            turtle.forward(h)

        def goto_position(x, y, turtle):
            turtle.penup()
            turtle.setposition(x, y)

        def set_random_color(turtle):
            turtle.color(
                "#{:02x}{:02x}{:02x}".format(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
            )

        screen = turtle.Screen()

        screen.title("Testing Turtle Again")
        screen.setup(width=600, height=600)
        screen.bgcolor("white")

        myturtle = turtle.Turtle()

        myturtle.speed(1)
        myturtle.goto(0, 0)
        myturtle.pensize(3)

        for rect in list_rectangles:
            set_random_color(myturtle)
            goto_position(rect.x, rect.y, myturtle)
            draw_rect(rect.width, rect.height, myturtle)

            goto_position(rect.x, rect.y + 40, myturtle)
            write_digits(rect.width, myturtle, distance=True, )

            goto_position(
                rect.x - (len(str(rect.y) * 60)) - 20, rect.y, myturtle
            )
            write_digits(rect.height, myturtle, distance=True, )

        for sqr in list_squares:
            set_random_color(myturtle)
            goto_position(sqr.x, sqr.y, myturtle)
            draw_rect(sqr.size, sqr.size, myturtle)

            goto_position(sqr.x + (sqr.width // 2), sqr.y + 40, myturtle)
            write_digits(sqr.size, myturtle, distance=True, )

        screen.mainloop()

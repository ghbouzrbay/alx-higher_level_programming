#!/usr/bin/python3

"""Defines a base class."""

import json
import csv
import turtle

class Base:
    """Represent the base model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_of_dictionaries):
        """Return the JSON serialization of a list of dictionaries."""
        if list_of_dictionaries is None or list_of_dictionaries == []:
            return "[]"
        return json.dumps(list_of_dictionaries)

    @classmethod
    def save_to_file(cls, list_of_objects):
        """Write the JSON serialization of a list of objects to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_of_objects is None or list_of_objects == []:
                json_file.write("[]")
            else:
                list_of_dicts = [obj.to_dictionary() for obj in list_of_objects]
                json_file.write(Base.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string."""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **attributes):
        """Return an instance instantiated from a dictionary of attributes."""
        if attributes and attributes != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
            else:
                instance = cls(1)
            instance.update(**attributes)
            return instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances instantiated from a file of JSON strings."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as json_file:
                list_of_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**dictionary) for dictionary in list_of_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_of_objects):
        """Write the CSV serialization of a list of objects to a file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csv_file:
            if list_of_objects is None or list_of_objects == []:
                csv_file.write("[]")
            else:
                fieldnames = []
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_of_objects:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances instantiated from a CSV file."""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                fieldnames = []
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                list_of_dicts = csv.DictReader(csv_file, fieldnames=fieldnames)
                list_of_dicts = [dict([(k, int(v)) for k, v in dictionary.items()])
                                  for dictionary in list_of_dicts]
                return [cls.create(**dictionary) for dictionary in list_of_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_of_rectangles, list_of_squares):
        """Draw rectangles and squares using the turtle module."""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rectangle in list_of_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rectangle.x, rectangle.y)
            turt.down()
            for _ in range(2):
                turt.forward(rectangle.width)
                turt.left(90)
                turt.forward(rectangle.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for square in list_of_squares:
            turt.showturtle()
            turt.up()
            turt.goto(square.x, square.y)
            turt.down()
            for _ in range(2):
                turt.forward(square.width)
                turt.left(90)
                turt.forward(square.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

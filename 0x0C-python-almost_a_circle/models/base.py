#!/usr/bin/python3
""" Base class created """

import json
import csv
import turtle

class Base:
    """ A base class for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionairies):
        if list_dictionairies is None:
            return "[]"
        else:
            return json.dumps(list_dictionairies)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves a list of objects to a JSON file"""
        if list_objs is None:
            list_objs = []

        """ Get the name of the class (cls) and create the filename """
        class_name = cls.__name__
        filename = f"{class_name}.json"

        """ Convert the list of object to a list of dictionaires"""
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        """ Convert the list of dictionaries to JSON string"""
        json_string = cls.to_json_string(list_dicts)

        """ Write the JSON string to te file"""
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List of dictionaries extracted from the JSON string.
        """
        if json_string is None:
            json_string = []
            return json_string
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes set from a dictionary.

        Args:
            **dictionary: Keyword arguments representing instance attributes.

        Returns:
            Base: An instance with attributes set from the dictionary.
        """
        dummy_instance = None
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        if dummy_instance is not None:
            # if 'id' in dictionary:
            print("Before update:", dummy_instance.__dict__)
            dummy_instance.update(**dictionary)
            print("After update:", dummy_instance.__dict__)
            return dummy_instance
        return None

    @classmethod
    def load_from_file(cls):
        """ Loads and returns a list of instance from a JSON file.

        Returns:
            list: List of instances loaded from the JSON file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                list_dicts = cls.from_json_string(json_data)
                intances = [cls.create(**data) for data in list_dicts]
                return intances
        # If there's no such file then just return empty list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves a list of objects to a CSV file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if cls .__name__ == 'Rectangle':
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == 'Square':
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        instances = []
        try:
            with open(filename, "r", newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        instance = cls(int(row[1]), int(row[2]), int(
                            row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == 'Square':
                        instance = cls(int(row[1]), int(
                            row[2]), int(row[3]), int(row[0]))
                    instances.append(instance)
            return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        # Initialize the turtle screen 
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        screen.title("Drawing Rectangles and Sqaures")

        # Create a turtle object for drawing
        t = turtle.Turtle()

        # Define a function to draw rectangle
        def draw_rectangle(rectangle):
            t.penup()
            t.goto(rectangle.x - rectangle.y)
            t.pendown()
            t.color("red")
            t.begin_fill
            for _ in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.end_fill()

        # Define a function to draw a sqaure
        def draw_square(sqare):
            t.penup()
            t.goto(square.c, square.y)
            t.pendown()
            t.color("purple")
            t.begin_fill()
            for _ in range(4):
                t.forward(sqaure.size)
                t.left(90)
            t.end_fill()

        # Draw all rectangles
        for rectangle in list_rectangles:
            draw_rectangle(rectangle)

        # Draw all squares
        for square in list_squares:
            draw_square(square)

        # Close the turtle graphics window when clicked
        screen.exitonclick()
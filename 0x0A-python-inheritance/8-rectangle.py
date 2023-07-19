#!/usr/bin/python3
""" Module for Geomerty """


class BaseGeometry:
    """ A class for geometry """

    def area(self):
        """ Method to calculate the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method to validate an integer value

        Args:
            name (str): The name of the value being validated
            value (int): The value to be validated

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is not greater than 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        super().__init__()
        self.width = width
        self.height = height
        self.integer_validator("width", self.width)
        self.integer_validator("height", self.height)

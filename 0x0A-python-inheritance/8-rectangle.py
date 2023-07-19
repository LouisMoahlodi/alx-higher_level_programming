#!/usr/bin/python3
""" Empty class"""


class BaseGeometry:
    """ A function for geometry """

    def area(self):
        """ Method to calculate the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method to validate an integer value """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

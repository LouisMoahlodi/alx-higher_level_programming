#!/usr/bin/python3
""" Empty class"""

class BaseGeometry:
    """ A function for geometry """

    def area(self):
        """ Method to calculate the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method to validate an integer value """
        if type(value) != int:
            raise TypeError(f"[TypeError] {name} must be an integer")
        elif value <= 0:
            raise ValueError(f"[VaulueError] {name}must be greater than 0")

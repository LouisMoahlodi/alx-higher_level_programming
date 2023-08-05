#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """this class represents a base geometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#The first block of code is the correct implementation for the task because it 
# directly checks if the type of value is exactly int, whereas the second block of code 
# checks if value is an instance of the int class. 

# class BaseGeometry:
#     """ A function for geometry """

#     def area(self):
#         """ Method to calculate the area """
#         raise Exception("area() is not implemented")

#     def integer_validator(self, name, value):
#         """ Method to validate an integer value """
#         if not isinstance(value, int):
#             raise TypeError(f"{name} must be an integer")
#         elif value <= 0:
#             raise ValueError(f"{name} must be greater than 0")

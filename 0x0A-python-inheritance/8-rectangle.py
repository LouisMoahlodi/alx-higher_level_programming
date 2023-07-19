#!/usr/bin/python3
""" Inherits from  BaseGeomerty """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
     """
        Initializes a Rectangle instance

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
     def __init__(self, width, height):
        """ Initializes a new Rectangle"""
        super().__init__()
        self.width = width
        self.height = height
        self.integer_validator("width", self.width)
        self.integer_validator("height", self.height)

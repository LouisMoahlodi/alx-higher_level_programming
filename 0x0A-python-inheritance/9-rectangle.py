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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Method to calculate the are of the rectangle.
        """
        return self.__width * self.__height
    
    def __str__(self):
        """ Returns string representation for Rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
    
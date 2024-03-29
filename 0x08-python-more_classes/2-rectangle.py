#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """ Intializing the class

        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width

        Raises:
            TypeError: if width is not an int
            ValueError: if width is less than 0
        """

        return self.__width

    @width.setter
    def width(self, value):

        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle

        Raises:
            TypeError: if height is not an int
            ValueError: if height is less o
        """

        return self.__height

    @height.setter
    def height(self, value):

        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area rectangle
        Returns: the area of a rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        "Represents the area of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

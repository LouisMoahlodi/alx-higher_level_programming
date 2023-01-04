#!/usr/bin/python3
""" Defines a square"""


class Square:
    """Represents a sqaure"""

    def __init__(self, size=0):
        """Initialzing the class
        Args:
            size - Represents the size of the square defined
        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than zero
        """
        self.__size = size

        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calcuate the area of the square

        Returns: the square of the size
        """
        return (self.__size ** 2)

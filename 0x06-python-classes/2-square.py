#!/usr/bin/python3
""" Defines a square & creates private insatnce attribute"""


class Square:
    """Represents a sqaure"""

    def __init__(self, size=0):
        """Initialzing the class
        Args: size - Represents the size of the square defined
        """
        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

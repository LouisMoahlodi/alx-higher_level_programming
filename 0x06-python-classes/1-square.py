#!/usr/bin/python3
""" Defines a square & creates private insatnce attribute"""


class Square:
    """Represents a sqaure"""

    def __init__(self, size):
        """Initialzing the class
        Args: size - Represents the size of the square defined
        """

        self.__size = size

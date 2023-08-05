#!/usr/bin/python3
""" Inherits from Rectnagle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Initializes sqaure instance
    Args:
        size (int): the size of the square using the area  function
    """

    def __init__(self, size):
        """
        Represents the square
        """
        self.integer_validator("size", size)
        self.__size = size

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
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns string representation for Sqaure
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
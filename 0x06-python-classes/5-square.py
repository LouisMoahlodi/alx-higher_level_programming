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

    @property
    def size(self):
        """Retrievs size of square"""

        return self.__size

    @size.setter
    def size(self, value):

        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcuate the area of the square

        Returns: the square of the size
        """
        return (self.__size ** 2)

    def my_print(self):

        if self.__size == 0:
            print()

        for i in range(self.__size):
                print('#' * self.__size)

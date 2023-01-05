#!/usr/bin/python3
""" Defines a square"""


class Square:
    """Represents a sqaure"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialzing the class
        Args:
            size - Represents the size of the square defined
        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than zero
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves the position of sqaure"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of this Square

        Args:
            value as a tuple of 2 positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tupe < 0
            """
        if not type(value) is tuple or len(value) != 2 or \
                not all([type(i) == int for i in value]) or \
                not all([i >= 0 for i in value]):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calcuate the area of the square

        Returns: the square of the size
        """
        return (self.__size ** 2)

    def my_print(self):

        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print('#' * self.__size)

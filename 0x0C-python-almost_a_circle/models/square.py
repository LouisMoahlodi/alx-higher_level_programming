#!/usr/bin/python3
"""
Module containing the Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square that inherits from Rectangle.

    Attributes:
        size (int): The size of the square's sides.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int, optional):
                The x-coordinate of the square's position. Defaults to 0.
            y (int, optional):
                The y-coordinate of the square's position. Defaults to 0.
            id (int, optional):
                The unique identifier of the square. Defaults to None.
        """
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: A string in the format "[Square] (id) x/y - size"
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

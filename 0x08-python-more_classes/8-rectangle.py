#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Intializing the class

        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Calculates the perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints area of rectangle with the '#' character"""
        if self.__width == 0 or self.__width == 0:
            return ""
        """rectangle = ""
        #for i in range(self.__height):
            #for j in range(self.width):
                #rectangle += "#"
            #if i < self.__height - 1:
                #rectangle += "\n"
        #return (rectangle)"""

        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """ return  a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints message when an instance is deleted"""
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 == rect_2:
            return rect_1

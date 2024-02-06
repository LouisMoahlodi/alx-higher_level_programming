#!/usr/bib/python3
class MyInt(int):
    """A class representing an integer with inverted equality and inequality operators.

    Inherits from the built-in int class.

    Attributes:
        Inherits all attributes from the int class.

    Methods:
        __eq__(self, other): Overrides the equality operator (==).
        __ne__(self, other): Overrides the inequality operator (!=).
    """

    def __eq__(self, other):
        """Override the equality operator.

        Args:
            other: The object to compare with self.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """Override the inequality operator.

        Args:
            other: The object to compare with self.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return not super().__ne__(other)

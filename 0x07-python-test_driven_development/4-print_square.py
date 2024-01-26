#!/usr/bin/python3

"""
This module Prints a square made of '#' characters with the given size

"""

def print_square(size):
    """
    Prints a square made of '#' characters with the given size.

    Args:
        size (int): The size of the square. It must be a non-negative integer.

    Returns:
        None

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(5)
        #####
        #####
        #####
        #####
        #####
    """
    # Check if size is an integer
    if type(size) != int:
        raise TypeError("size must be an integer")

    # Check if size is non-negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if size is a non-negative integer
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")

    # If size is 0, return None (no square to print)
    if size == 0:
        return None

    else:
        # Print Square
        for i in range(size):
            print('#' * size)

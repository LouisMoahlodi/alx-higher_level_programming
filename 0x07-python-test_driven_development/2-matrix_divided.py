#!/usr/bin/python3
"""

This module provides a function for dividing all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of int or float): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists of float: The divided matrix.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   or if each row of the matrix is not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(x, (int, float))
               for x in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix is of the same size
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and rounding to 2 decimal places
    divided_matrix = [[round(element / div, 2)
                       for element in row] for row in matrix]

    return divided_matrix

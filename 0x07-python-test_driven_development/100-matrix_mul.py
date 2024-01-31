#!/usr/bin/python3
"""
Module to multiply two martrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.
    Parameters:
        - m_a (list of integers or floats) : The first matrix to multiply
        - m_b (list of integers or floats) : The second matrix to multiply
    Returns:
        A new list representing the result of multiplying m_a by m_b
    """

    # Check if arguments are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if arguments are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if arguments are not empty lists
    if not m_a or not all(m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not all(m_b):
        raise ValueError("m_b can't be empty")

    # Check if all elements in arguments are integers or floats
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check if each row of m_a has the same size
    row_size_a = len(m_a[0])
    if not all(len(row) == row_size_a for row in m_a):
        raise ValueError("each row of m_a must be of the same size")

    # Check if each row of m_b has the same size
    row_size_b = len(m_b[0])
    if not all(len(row) == row_size_b for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize the result matrix with zeros
    result = [[0] * len(m_b[0]) for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

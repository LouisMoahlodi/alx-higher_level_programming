#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix of the same size as the input matrix
    new_matrix = matrix.copy()

# Compute the square value of each integer in the matrix
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x ** 2, matrix[i]))

    return new_matrix

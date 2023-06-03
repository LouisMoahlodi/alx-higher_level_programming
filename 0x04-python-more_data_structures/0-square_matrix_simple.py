#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
# Create a new matrix of the same size as the input matrix
	result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

# Compute the square value of each integer in the matrix
for i in range(len(matrix)):
	for j in range(len(matrix)):
		result[i][j] = matrix[i][j] ** 2
	return result


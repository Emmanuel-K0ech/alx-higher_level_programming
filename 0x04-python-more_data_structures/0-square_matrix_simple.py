#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []
    for i in range(len(matrix)):
        new_matrix = []
        for j in matrix[i]:
            new_matrix.append(j * j)
        result_matrix.append(new_matrix)
    return result_matrix

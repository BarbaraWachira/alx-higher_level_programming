#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []

    if not isinstance(matrix, list):
        print("Matrix is not a list")
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for k in i:
            if not isinstance(k, int) and not isinstance(k, float):
                print("Not list of lists or not integers")
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
            break
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        row = []
        for k in i:
            row.append(round(k / div, 2))
        new_matrix.append(row)
        row = []

    return new_matrix

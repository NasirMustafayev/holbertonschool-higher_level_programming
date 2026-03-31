#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix by a given divisor.
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 2)
[[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    """
    result = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []

        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
            
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(num / div, 2))
        result.append(new_row)
    
    return result

#!/usr/bin/python3
"""
This module contains a function that generates the Pascal's triangle of a given size.
"""

def pascal_triangle(n):
    """Generates the Pascal's triangle of a given size."""
    if n <= 0:
        return []
    result = []

    for row_num in range(n):

        row = [1] * (row_num + 1)

        for j in range(1, row_num):
            row[j] = result[row_num - 1][j - 1] + result[row_num - 1][j]

        result.append(row)

    return result

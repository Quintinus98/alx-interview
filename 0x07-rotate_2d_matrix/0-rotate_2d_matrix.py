#!/usr/bin/env python3
"""Rotate a 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty."""
    rows = len(matrix)
    for i in range(rows):
        for j in range(i, rows):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(rows):
        matrix[i].reverse()

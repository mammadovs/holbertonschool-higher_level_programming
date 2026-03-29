#!/usr/bin/python3
"""Module for matrix division."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number."""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    row_size = None
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg_type)

    return [[round(item / div, 2) for item in row] for row in matrix]

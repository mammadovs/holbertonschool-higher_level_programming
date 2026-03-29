#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
It handles various edge cases including division by infinity and 
ensures output consistency with rounding.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor (div).

    Args:
        matrix (list of lists): A list containing lists of integers or floats.
        div (int/float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix representing the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is zero.
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    # Validate if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate if matrix is a list and not empty
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    row_size = None
    for row in matrix:
        # Check if each row is a list and not empty
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)

        # Set or validate row size consistency
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError(msg_size)

        # Validate each element in the row is a number
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg_type)

    # Perform division, round to 2 decimal places, and handle -0.0
    # Adding 0.0 converts -0.0 (from negative / inf) to 0.0
    return [[round((item / div) + 0.0, 2) for item in row] for row in matrix]

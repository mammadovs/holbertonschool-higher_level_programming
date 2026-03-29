#!/usr/bin/python3
"""
Module 2-matrix_divided
This module provides a function that divides all elements of a matrix.
It checks for type safety and proper matrix dimensions.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int, float): The number to divide by.

    Returns:
        list: A new matrix with results rounded to 2 decimal places.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix or not matrix[0]:
        raise TypeError(error_msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])

    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix

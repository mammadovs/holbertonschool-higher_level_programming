#!/usr/bin/python3
"""
Module 2-matrix_divided
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Проверка: является ли matrix списком и не пуст ли он
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # 2. Проверка: каждый элемент matrix должен быть списком
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)

    # 3. Проверка: div должен быть числом
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 4. Проверка: деление на ноль
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 5. Проверка: одинаковый размер строк
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # 6. Проверка: элементы внутри строк — числа + само деление
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)

    return new_matrix

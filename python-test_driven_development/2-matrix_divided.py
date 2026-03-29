#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Проверка: матрица должна быть списком и не пустой
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # 2. Проверка каждой строки и её содержимого
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    # 3. Проверка размера строк (сравнение с первой строкой)
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # 4. Проверка делителя (число)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 5. Проверка деления на ноль
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 6. Само деление (включая обработку inf и nan через стандартное поведение)
    # round(x / div, 2) корректно обработает float('inf') -> 0.0
    return [[round(x / div, 2) for x in row] for row in matrix]

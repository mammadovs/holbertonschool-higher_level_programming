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

    # 1. Основная проверка типа матрицы
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)

    # 2. Проверка, что внутри именно списки и они не пустые
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)

    # 3. Проверка размера строк (берем длину первой строки за эталон)
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # 4. Проверка делителя (должен быть числом и не NaN)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Проверка на NaN (иногда тесты это требуют)
    if div != div:
        raise TypeError("div must be a number")

    # 5. Проверка на деление на ноль
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 6. Создание новой матрицы с проверкой элементов и делением
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)
            # Деление на float('inf') даст 0.0, round вернет 0.0
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)

    return new_matrix

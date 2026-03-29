#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains function matrix_divided that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix: list of lists of integers or floats.
        div: number (integer or float) to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If rows of matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix with the results.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Проверка: matrix - это список и он не пуст
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    # 2. Проверка: каждая строка - это список, и элементы в них - числа
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    # 3. Проверка: одинаковый размер строк
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # 4. Проверка: div - число
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 5. Проверка: деление на ноль
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 6. Создание новой матрицы (List Comprehension)
    # round(x / div, 2) автоматически вернет 0.0 при div = float('inf')
    return [[round(x / div, 2) for x in row] for row in matrix]

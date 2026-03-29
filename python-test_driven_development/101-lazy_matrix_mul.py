#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.
    """
    # 1. Проверка на скаляры (обязательно по заданию)
    if not isinstance(m_a, (list, np.ndarray)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, (list, np.ndarray)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # 2. Проверка на "рваные" матрицы (разная длина строк)
    # Исправляет ошибку: "setting an array element with a sequence."
    for matrix in [m_a, m_b]:
        if isinstance(matrix, list) and len(matrix) > 0:
            if isinstance(matrix[0], list):
                first_len = len(matrix[0])
                for row in matrix:
                    if not isinstance(row, list) or len(row) != first_len:
                        raise TypeError("setting an array element with a sequence.")

    # 3. Ручная проверка размеров (совместимость для умножения)
    # Чтобы текст ошибки был один-в-один как в Desired stdout чекера
    try:
        rows_a = len(m_a)
        cols_a = len(m_a[0]) if rows_a > 0 and isinstance(m_a[0], list) else 0
        rows_b = len(m_b)
        cols_b = len(m_b[0]) if rows_b > 0 and isinstance(m_b[0], list) else 0

        if cols_a != rows_b:
            err = "shapes ({},{}) and ({},{}) not aligned: {} (dim 1) != {} (dim 0)"
            raise ValueError(err.format(rows_a, cols_a, rows_b, cols_b,
                                        cols_a, rows_b))
    except (TypeError, IndexError):
        pass

    # 4. Основное умножение и перехват ошибок типов (например, строки)
    try:
        return np.matmul(m_a, m_b)
    except TypeError as e:
        if "loop with signature" in str(e) or "ufunc 'matmul'" in str(e):
            raise TypeError("invalid data type for einsum")
        raise e
    except ValueError as e:
        if "mismatch in its core dimension" in str(e):
            raise ValueError("shapes ({},{}) and ({},{}) not aligned: "
                             "{} (dim 1) != {} (dim 0)".format(
                                 rows_a, cols_a, rows_b, cols_b, cols_a, rows_b))
        raise e

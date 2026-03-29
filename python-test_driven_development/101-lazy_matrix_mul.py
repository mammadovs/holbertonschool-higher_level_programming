#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.
    """
    # 1. Проверка на скаляры
    if not isinstance(m_a, (list, np.ndarray)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, (list, np.ndarray)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # 2. Проверка на "рваные" матрицы
    for matrix in [m_a, m_b]:
        if isinstance(matrix, list) and len(matrix) > 0:
            if isinstance(matrix[0], list):
                row_len = len(matrix[0])
                for row in matrix:
                    if not isinstance(row, list) or len(row) != row_len:
                        raise TypeError("setting an array element with a "
                                        "sequence.")

    # 3. Ручная проверка размеров (совместимость)
    try:
        r_a, c_a = len(m_a), len(m_a[0]) if len(m_a) > 0 else 0
        r_b, c_b = len(m_b), len(m_b[0]) if len(m_b) > 0 else 0

        if c_a != r_b:
            err = ("shapes ({},{}) and ({},{}) not aligned: "
                   "{} (dim 1) != {} (dim 0)")
            raise ValueError(err.format(r_a, c_a, r_b, c_b, c_a, r_b))
    except (TypeError, IndexError):
        pass

    # 4. Основное умножение
    try:
        return np.matmul(m_a, m_b)
    except TypeError as e:
        if "loop with signature" in str(e) or "ufunc 'matmul'" in str(e):
            raise TypeError("invalid data type for einsum")
        raise e
    except ValueError as e:
        if "mismatch in its core dimension" in str(e):
            err = ("shapes ({},{}) and ({},{}) not aligned: "
                   "{} (dim 1) != {} (dim 0)")
            raise ValueError(err.format(r_a, c_a, r_b, c_b, c_a, r_b))
        raise e

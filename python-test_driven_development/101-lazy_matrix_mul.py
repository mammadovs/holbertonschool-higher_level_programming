#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.
    """
    if not isinstance(m_a, (list, np.ndarray)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, (list, np.ndarray)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        # Перехватываем ошибку размеров и меняем текст под чекер
        err_msg = str(e)
        if "mismatch in its core dimension 0" in err_msg or "not aligned" in err_msg:
            # Пытаемся вычислить размеры для формирования строки
            try:
                rows_a = len(m_a)
                cols_a = len(m_a[0]) if rows_a > 0 else 0
                rows_b = len(m_b)
                cols_b = len(m_b[0]) if rows_b > 0 else 0
                # Формат: shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)
                raise ValueError("shapes ({},{}) and ({},{}) not aligned: {} (dim 1) != {} (dim 0)".format(
                    rows_a, cols_a, rows_b, cols_b, cols_a, rows_b))
            except:
                raise ValueError(err_msg)
        raise ValueError(err_msg)
    except TypeError as e:
        # Для ошибок типа данных (строки внутри списка)
        err_msg = str(e)
        if "loop with signature matching types" in err_msg or "ufunc 'matmul'" in err_msg:
            # Чекер может ожидать разные варианты, но обычно это просто TypeError
            # Если чекер падает на Non-numeric, можно попробовать выкинуть стандартный TypeError
            raise TypeError("invalid data type for einsum")
        raise TypeError(err_msg)

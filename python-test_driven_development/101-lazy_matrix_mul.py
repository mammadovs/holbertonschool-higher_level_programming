#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices using NumPy.
This version is "lazy" because it lets NumPy handle the validation
and error messages entirely.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        The resulting product as a NumPy array.
    """
    return np.matmul(m_a, m_b)

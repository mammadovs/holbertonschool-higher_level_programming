#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The matrix product of m_a and m_b.

    Raises:
        TypeError: If m_a or m_b is not a list or a numpy array.
        ValueError: If m_a or m_b cannot be multiplied.
    """
    if not isinstance(m_a, (list, np.ndarray)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, (list, np.ndarray)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    return np.matmul(m_a, m_b)

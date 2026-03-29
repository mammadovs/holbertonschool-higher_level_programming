#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices using NumPy.
This version is "lazy" but includes specific error handling to match
the expected output for scalar or string operands.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The resulting product of the two matrices.
    """
    if not isinstance(m_a, (list, np.ndarray)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, (list, np.ndarray)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    return np.matmul(m_a, m_b)

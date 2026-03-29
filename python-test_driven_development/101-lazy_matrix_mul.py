#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices using NumPy.
This approach leverages the NumPy library for high-performance
computation and built-in validation.
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
    return np.matmul(m_a, m_b)

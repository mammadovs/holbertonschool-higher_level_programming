#!/usr/bin/python3
"""
This module contains a function for matrix multiplication.
It provides strict validation for input types, empty matrices,
non-numeric elements, and dimensional compatibility.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices: m_a and m_b.

    Args:
        m_a (list of lists): The first matrix (integers or floats).
        m_b (list of lists): The second matrix (integers or floats).

    Raises:
        TypeError: If inputs are not lists, not lists of lists,
                   contain non-numbers, or are not rectangular.
        ValueError: If matrices are empty or cannot be multiplied.

    Returns:
        list of lists: The resulting product of m_a * m_b.
    """
    # 1. Validate list type
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. Validate list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. Validate not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. Validate numeric contents
    for row in m_a:
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError("m_b should contain only integers or floats")

    # 5. Validate rectangular shape
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 6. Validate multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiplication Logic
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            dot_product = 0
            for k in range(len(m_b)):
                dot_product += m_a[i][k] * m_b[k][j]
            new_row.append(dot_product)
        result.append(new_row)

    return result

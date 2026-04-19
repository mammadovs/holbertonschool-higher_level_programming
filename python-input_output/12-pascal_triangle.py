#!/usr/bin/python3
"""
Module for Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        # Start the row with 1
        row = [1]

        # Calculate the middle elements
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        # End the row with 1
        row.append(1)
        triangle.append(row)

    return triangle

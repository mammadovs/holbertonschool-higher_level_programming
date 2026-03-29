#!/usr/bin/python3
"""
This module provides a function that prints a square with #.
The module includes validation for the size argument to ensure it is
a non-negative integer.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The length of the side of the square.

    Raises:
        TypeError: If size is not an integer or is a negative float.
        ValueError: If size is less than 0.
    """
    if (isinstance(size, float) and size < 0) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

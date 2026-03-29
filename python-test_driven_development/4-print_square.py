#!/usr/bin/python3
"""
This module contains a function that prints a square with #.
The module handles type and value validation for the size argument.
"""


def print_square(size):
    """
    Prints a square using the '#' character based on the size provided.

    Args:
        size (int): The side length of the square to print.

    Raises:
        TypeError: If size is not an integer or is a negative float.
        ValueError: If size is a negative integer.
    """
    if (isinstance(size, float) and size < 0) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

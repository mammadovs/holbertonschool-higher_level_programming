#!/usr/bin/python3
"""
Module 2-square

This module defines a class Square that represents a square shape.
The square has a private attribute `__size` to store its size,
which must be a non-negative integer.
"""


class Square:
    """
    Class Square represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        The size must be an integer greater than or equal to 0.

        Args:
            size (int): Optional. The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

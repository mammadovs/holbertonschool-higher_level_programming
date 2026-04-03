#!/usr/bin/python3
"""
Module 1-square

Defines a class Square with a private size attribute.
This class represents a square and stores its size internally.
"""


class Square:
    """
    Class Square represents a square.

    The square has a private attribute `__size` that stores its size.
    Currently, there are no methods to modify or retrieve the size.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance with a given size.

        Args:
            size: The size of the square (no type or value checks applied).
        """
        self.__size = size

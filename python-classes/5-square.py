#!/usr/bin/python3
"""
Module 5-square

This module defines a class Square that represents a square shape.
The square has a private attribute `__size` to store its size.
A property is provided to safely get and set the size with validation.
The class also provides methods to compute the area and print
the square using the '#' character.
"""


class Square:
    """
    Class Square represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (private).

    Properties:
        size (int): Get or set the size of the square with validation.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        The size must be a non-negative integer. If no size is provided,
        it defaults to 0. Validation is performed using the size setter.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print('#' * self.__size)

#!/usr/bin/python3
"""
Module 6-square

This module defines a class Square that represents a square with a size
and a position. The square can calculate its area and be printed using
the '#' character at the specified position offset.
"""


class Square:
    """
    Represents a square with a private size and position.

    Attributes:
        __size (int): The size of the square's sides (private).
        __position (tuple): The (x, y) offset for printing (private).

    Properties:
        size (int): Get or set the size with validation.
        position (tuple): Get or set the position with validation.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square.

        Args:
            size (int, optional): Side length of the square (default 0).
            position (tuple, optional): Printing offset as (x, y)
                                        (default (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
                       of 2 non-negative integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the current printing position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the printing position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square (size squared)."""
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        Respects the position offset:
          - position[0] adds spaces before each row
          - position[1] adds blank lines before the square
        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print each row of the square with horizontal offset
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)

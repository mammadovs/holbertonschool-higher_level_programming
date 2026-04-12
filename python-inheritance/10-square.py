#!/usr/bin/python3
"""
Module 10-square
Contains class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square that inherits from Rectangle"""

    def __init__(self, size):
        """
        Initialize a new Square
        Args:
            size (int): The dimension of the square's sides
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

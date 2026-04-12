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
        # Validate size using the inherited integer_validator
        self.integer_validator("size", size)
        
        # Initialize the parent Rectangle with size as both width and height
        super().__init__(size, size)
        
        # Assign to private attribute
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

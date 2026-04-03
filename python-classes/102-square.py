#!/usr/bin/python3
"""Define a class Square with size and area-based comparisons."""


class Square:
    """Represent a square with a size and area-based comparison."""

    def __init__(self, size=0):
        """Initialize a square with an optional size."""
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size должен быть числом")
        if value < 0:
            raise ValueError("size должен быть >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    # Comparison operators based on area
    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

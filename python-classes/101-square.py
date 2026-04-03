#!/usr/bin/python3
"""Define a class Square with size and position, supporting printing."""


class Square:
    """Represent a square with a size and a position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with optional size and position.

        Args:
            size (int): The size of the square's sides (default 0).
            position (tuple): Horizontal and vertical offsets (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' considering its position."""
        if self.__size == 0:
            print()
            return

        # print vertical offset
        for _ in range(self.__position[1]):
            print()

        # print each row with horizontal offset
        for _ in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size
            print(line)

    def __str__(self):
        """Return string representation of the square (like my_print)."""
        if self.__size == 0:
            return ""

        lines = [""] * self.__position[1]  # vertical offset
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)

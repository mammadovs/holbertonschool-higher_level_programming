#!/usr/bin/python3
"""Module defining a Rectangle class with width, height, area, perimeter,
string representation, repr, deletion message, instance counter, print symbol,
comparison by area, and a class method to create squares."""


class Rectangle:
    """Represent a rectangle with width and height, count instances,
    print symbol, comparison by area, and square creation."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): optional width of the rectangle
            height (int): optional height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        If width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string of the rectangle using print_symbol.

        If width or height is 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = []
        for _ in range(self.__height):
            row = str(self.print_symbol) * self.__width
            lines.append(row)
        return "\n".join(lines)

    def __repr__(self):
        """Return a string representation to recreate a new instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and update instance counter on deletion."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area.

        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle

        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle instance

        Returns:
            Rectangle: the bigger rectangle or rect_1 if equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)

#!/usr/bin/python3
"""
This module demonstrates abstract base classes, duck typing,
and geometric calculations for shapes.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for all geometric shapes.
    """

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Represents a circle. Handles negative radius by using its absolute value.
    """

    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = abs(radius)

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle with a given width and height.
    """

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints area and perimeter of a shape using duck typing.

    Args:
        shape: An object that is expected to have area() and perimeter()
               methods (duck typing).
    """
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")


# Testing the implementation
if __name__ == "__main__":
    my_circle = Circle(-5)  # Test negative radius
    my_rectangle = Rectangle(4, 6)

    print("Circle Info:")
    shape_info(my_circle)

    print("\nRectangle Info:")
    shape_info(my_rectangle)

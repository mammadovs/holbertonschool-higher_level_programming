#!/usr/bin/python3
"""
This module demonstrates abstract base classes and duck typing
using geometric shapes.
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
    Represents a circle with a given radius.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle with a given width and height.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.
    It doesn't check if 'shape' is an instance of Shape,
    it just calls the required methods.
    """
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")


# Testing the implementation
if __name__ == "__main__":
    my_circle = Circle(5)
    my_rectangle = Rectangle(4, 6)

    print("Circle Info:")
    shape_info(my_circle)

    print("\nRectangle Info:")
    shape_info(my_rectangle)

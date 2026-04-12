#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
It serves as a foundational class for various geometric shapes.
"""


class BaseGeometry:
    """
    A base class for geometry objects.
    Provides a blueprint for area calculation and attribute validation.
    """

    def area(self):
        """
        Public instance method to calculate the area.
        Currently not implemented and raises an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the parameter (assumed to be a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

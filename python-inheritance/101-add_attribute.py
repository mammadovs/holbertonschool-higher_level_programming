#!/usr/bin/python3
"""
This module provides a function to dynamically add attributes to objects.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to receive the new attribute.
        name: The name of the attribute (string).
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

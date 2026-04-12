#!/usr/bin/python3
"""
This module provides a function to lookup object attributes.
"""


def lookup(obj):
    """
    Returns a list object containing the available
    attributes and methods of an object.
    """
    # The dir() function returns a list of valid attributes of the object
    return dir(obj)

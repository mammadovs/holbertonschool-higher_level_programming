#!/usr/bin/python3
"""
This is the 3-say_my_name module.
This module supplies one function, say_my_name(), which prints a specific string
using a first name and an optional last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>"

    Args:
        first_name (str): The first name string.
        last_name (str): The last name string (optional).

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

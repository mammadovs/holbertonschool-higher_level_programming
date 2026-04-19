#!/usr/bin/python3
"""
Module containing a function that returns the dictionary description
of an object for JSON serialization.
"""


def class_to_json(obj):
    """Returns the dictionary description of an instance of a Class."""
    return obj.__dict__

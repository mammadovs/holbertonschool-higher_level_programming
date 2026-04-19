#!/usr/bin/python3
"""
Module that defines a Student class with attribute filtering.
"""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for k in attrs:
                if k in self.__dict__:
                    res[k] = self.__dict__[k]
            return res
        return self.__dict__

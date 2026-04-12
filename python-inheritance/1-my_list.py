#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
"""


class MyList(list):
    """A subclass of list with an additional sorted printing method."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))

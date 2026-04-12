#!/usr/bin/python3
"""
This module defines the MyInt class.
"""


class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted.
    """

    def __eq__(self, other):
        """Override == with != behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != with == behavior."""
        return super().__eq__(other)

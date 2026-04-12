#!/usr/bin/python3
class MyInt(int):
    """
    A rebellious integer where equality is flipped.
    """

    def __eq__(self, other):
        # We use the parent (int) class to check equality,
        # then return the opposite.
        return not super().__eq__(other)

    def __ne__(self, other):
        # Similarly, we return the opposite of the
        # standard inequality check.
        return not super().__ne__(other)

#!/usr/bin/python3
"""
This module defines the VerboseList class, which extends the built-in list
to provide notifications when the list is modified.
"""


class VerboseList(list):
    """
    A list subclass that prints messages when items are added or removed.
    """

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list")

    def extend(self, items):
        """Extends the list and prints the number of items added."""
        count = len(items)
        super().extend(items)
        print(f"Extended the list with [{count}] items")

    def remove(self, item):
        """Prints a notification before removing a specific item."""
        print(f"Removed [{item}] from the list")
        super().remove(item)

    def pop(self, index=-1):
        """Prints a notification before popping an item."""
        item = self[index]
        print(f"Popped [{item}] from the list")
        return super().pop(index)


# Testing the implementation
if __name__ == "__main__":
    vl = VerboseList()

    vl.append(10)          # Added [10] to the list
    vl.extend([20, 30])    # Extended the list with [2] items
    vl.remove(20)          # Removed [20] from the list
    vl.pop()               # Popped [30] from the list

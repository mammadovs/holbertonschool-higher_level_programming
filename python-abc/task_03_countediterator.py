#!/usr/bin/python3
"""
This module defines the CountedIterator class, which wraps an iterator
to keep track of the number of items processed.
"""


class CountedIterator:
    """
    An iterator wrapper that counts how many items have been retrieved.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator and the counter.

        Args:
            iterable: Any iterable object (list, tuple, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the current number of items iterated."""
        return self.count

    def __next__(self):
        """
        Increments the counter and returns the next item.
        Raises StopIteration if there are no more items.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            # Re-raise StopIteration to signal the end of the iterator
            raise StopIteration

    def __iter__(self):
        """Makes the class itself an iterator."""
        return self


# Testing the implementation
if __name__ == "__main__":
    data = [10, 20, 30, 40]
    counted_iter = CountedIterator(data)

    print(f"Initial count: {counted_iter.get_count()}")

    # Manual calls
    print(f"First item: {next(counted_iter)}")
    print(f"Second item: {next(counted_iter)}")
    print(f"Current count: {counted_iter.get_count()}")

    # Iterating through the rest
    print("Remaining items:")
    for item in counted_iter:
        print(item)

    print(f"Final count: {counted_iter.get_count()}")

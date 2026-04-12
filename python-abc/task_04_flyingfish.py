#!/usr/bin/python3
"""
This module demonstrates multiple inheritance in Python using
Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish, inheriting from both Fish and Bird.
    Demonstrates overriding methods from multiple parents.
    """

    def fly(self):
        """Overrides Bird's fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides Fish's swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides habitat method from both parents."""
        print("The flying fish lives both in water and the sky!")


# Testing the implementation
if __name__ == "__main__":
    my_flying_fish = FlyingFish()

    # Calling overridden methods
    my_flying_fish.fly()
    my_flying_fish.swim()
    my_flying_fish.habitat()

    # Investigating Method Resolution Order (MRO)
    print("\nMethod Resolution Order (MRO):")
    print(FlyingFish.mro())

#!/usr/bin/python3
"""
This module demonstrates the use of mixins to grant a Dragon class
the ability to fly and swim using multiple inheritance.
"""


class SwimMixin:
    """Provides swimming functionality."""

    def swim(self):
        """Prints swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying functionality."""

    def fly(self):
        """Prints flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that combines swimming and flying abilities
    through mixins, and adds its own unique behavior.
    """

    def roar(self):
        """Prints the dragon's unique roar."""
        print("The dragon roars!")


# Testing the implementation
if __name__ == "__main__":
    # Create an instance of Dragon named Draco
    draco = Dragon()

    # Demonstrating Draco's abilities
    draco.swim()  # From SwimMixin
    draco.fly()   # From FlyMixin
    draco.roar()  # From Dragon class

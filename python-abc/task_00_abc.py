#!/usr/bin/python3
"""
This module defines an abstract base class Animal and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Subclass representing a dog.
    """

    def sound(self):
        """
        Returns the sound made by a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclass representing a cat.
    """

    def sound(self):
        """
        Returns the sound made by a cat.
        """
        return "Meow"

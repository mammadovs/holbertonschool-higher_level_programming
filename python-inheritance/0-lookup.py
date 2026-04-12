#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list object containing the available
    attributes and methods of an object.
    """
    # The dir() function returns a list of valid attributes of the object
    return dir(obj)

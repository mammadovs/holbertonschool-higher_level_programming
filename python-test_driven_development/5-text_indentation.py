#!/usr/bin/python3
"""
This module provides a function for text indentation.
It splits text based on specific characters: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The string to be formatted and printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = [".", "?", ":"]
    i = 0
    text = text.strip()

    while i < len(text):
        print(text[i], end="")
        if text[i] in special_chars:
            print("\n")
            if i + 1 < len(text) and text[i + 1] == " ":
                while i + 1 < len(text) and text[i + 1] == " ":
                    i += 1
        i += 1

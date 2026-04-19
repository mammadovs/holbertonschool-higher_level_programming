#!/usr/bin/python3
"""
Module that contains a function to insert a line after specific strings.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each line containing search_string."""
    text = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

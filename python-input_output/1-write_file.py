#!/usr/bin/python3
"""
Defines a function that writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written
    """
    with open(filename, "w") as file:
        return file.write(text)

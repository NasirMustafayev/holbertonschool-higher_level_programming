#!/usr/bin/python3
"""This module contains a function that appends a string to a text file"""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns the number of characters"""
    with open(filename, "a") as file:
        return file.write(text)

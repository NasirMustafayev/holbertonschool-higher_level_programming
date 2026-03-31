#!/usr/bin/python3
"""
Defines a function that prints a square of a given size using the '#' character
>>> print_square(3)
###
###
###
"""


def print_square(size):
    """
    Prints a square of a given size using the '#' character.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

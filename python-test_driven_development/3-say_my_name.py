#!/usr/bin/python3
"""
This module defines a function that prints a person's name in a specific format
>>> say_my_name("John", "Doe")
My name is John Doe
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a person's name in the format "My name is <first_name> <last_name>"
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

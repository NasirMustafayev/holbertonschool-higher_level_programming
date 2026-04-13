#!/usr/bin/python3
"""
Defining a function for exact instance check
"""


def is_same_class(obj, a_class):
    """Returns True if the obj is exact of a_class"""
    return type(obj) is a_class

#!/usr/bin/python3
"""
Defining a function for kind of instance check
"""


def inherits_from(obj, a_class):
    """Return True if the obj is an instance of a class that inherited"""
    return issubclass(obj, a_class)

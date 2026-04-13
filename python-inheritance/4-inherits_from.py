#!/usr/bin/python3
"""Defines a function that checks inheritance"""


def inherits_from(obj, a_class):
    """Returns True if obj is instance of inherited class"""
    return isinstance(obj, a_class) and type(obj) is not a_class

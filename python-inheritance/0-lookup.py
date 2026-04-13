#!/usr/bin/python3
"""
Defines a function that returns available attributes of object
"""


def lookup(obj):
    """Returns list of attributes"""
    return dir(obj)

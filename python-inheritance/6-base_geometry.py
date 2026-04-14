#!/usr/bin/python3
"""
Defines empty class BaseGeometry
"""


class BaseGeometry:
    """Raising an area exception"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

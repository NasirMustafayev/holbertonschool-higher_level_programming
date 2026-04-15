#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square, inheriting from Rectangle"""
    def __init__(self, size):
        """Initialize a Square instance with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

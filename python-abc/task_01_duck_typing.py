#!/usr/bin/python3
"""
This module defines an abstract base class `Shape` and two concrete classes
`Circle` and `Rectangle` that inherit from `Shape`.
It also includes a function `shape_info` that prints the area
and perimeter of a given shape instance.
 """
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Concrete class representing a circle."""
    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Concrete class representing a rectangle."""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__height + self.__width)


"""
Duck typing function that takes an instance of a shape
and prints its area and perimeter.
"""


def shape_info(shape):
    """Prints the area and perimeter of a shape instance."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

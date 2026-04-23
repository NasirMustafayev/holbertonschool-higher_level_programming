#!/usr/bin/python3
"""
Defines a Student class
with attributes first_name, last_name, and age,
and a method to_json that returns a dictionary representation of the instance.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    to_json method returns a dictionary representation of the instance.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

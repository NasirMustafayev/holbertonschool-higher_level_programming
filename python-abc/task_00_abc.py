#!/usr/bin/python3
"""Module that defines an abstract class and its subclasses"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal"""
    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses"""
        pass


class Dog(Animal):
    """Class representing a dog, subclass of Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Class representing a cat, subclass of Animal"""
    def sound(self):
        return "Meow"

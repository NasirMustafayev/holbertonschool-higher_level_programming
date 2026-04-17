#!/usr/bin/python3
"""
Defines FlyingFish class that inherits from both Fish and Bird classes
"""


class Fish:
    """
    Definesh Fish class and its methods
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Defines Bird class and its methods
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Defines FlyingFish class and ovverrides inherited methods
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

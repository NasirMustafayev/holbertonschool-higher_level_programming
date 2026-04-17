#!/usr/bin/python3
"""
Defines Dragon class that inherits from mixins called Swim and Fly
"""


class SwimMixin:
    """Defines SwimMixin class"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Defines FlyMixin class"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Defines Dragon class"""
    def roar(self):
        print("The dragon roars!")

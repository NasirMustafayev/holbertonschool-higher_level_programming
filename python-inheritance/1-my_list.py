#!/usr/bin/python3
"""
Defining class thats inherits from builtin list class
"""


class MyList(list):
    """Works with normal list methods and sorting them,printing them"""
    def print_sorted(self):
        print(sorted(self))

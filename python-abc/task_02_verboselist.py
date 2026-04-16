#!/usr/bin/python3
"""
This module defines a class VerboseList
that inherits from the built-in list class.
"""


class VerboseList(list):
    """
    A list that prints a message whenever an item is added, removed, or popped.
    """
    def append(self, item):
        """
        Override the append method to print a message when an item is added.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """
        Override the extend method to print a message when items are added.
        """
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def pop(self, item=-1):
        """
        Override the pop method to print a message when an item is popped.
        """
        popped = super().pop(item)
        print("Popped [{}] from the list.".format(popped))

    def remove(self, item):
        """
        Override the remove method to print a message when an item is removed.
        """
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

#!/usr/bin/python3
"""
Module that defines a class CountedIterator that counts the number of
iterations made over an iterable object.
"""


class CountedIterator:
    """
    Class that counts the number of iterations made over an iterable object.
    """
    def __init__(self, data):
        self.__iterator = iter(data)
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.__iterator)
        self.__counter += 1
        return item

    def get_count(self):
        return self.__counter

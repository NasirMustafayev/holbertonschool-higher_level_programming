#!/usr/bin/env python3
"""Pickle serialization"""
from fileinput import filename
import pickle


def serialize(self, filename):
    """Serializes a Python object to a file using pickle.

    Args:
        filename: The name of the file where the object will be serialized.
    """
    with open(filename, 'wb') as f:
        pickle.dump(self, f)


@classmethod
def deserialize(cls, filename):
    """Deserializes a Python object from a file using pickle.

    Args:
        filename: The name of the file from which to deserialize the object.
    Returns:
        The Python object deserialized from the file.
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)

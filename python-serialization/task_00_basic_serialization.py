#!/usr/bin/env python3
"""Basic serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python object to a JSON string and saves it to a file.

    Args:
        data: The Python object to serialize.
        filename: The name of the file where the JSON string will be saved.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize_file(filename):
    """Loads a JSON string from a file and deserializes it to a Python object.

    Args:
        filename: The name of the file from which to load the JSON string.

    Returns:
        The Python object deserialized from the JSON string.
    """
    with open(filename, 'r') as f:
        return json.load(f)

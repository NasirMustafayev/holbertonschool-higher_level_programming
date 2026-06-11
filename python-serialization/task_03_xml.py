#!/usr/bin/env python3
"""XML serialization"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary to XML format and saves it to a file.
    Args:
        dictionary: The Python dictionary to serialize.
        filename: The name of the file where the XML will be saved.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        item = ET.SubElement(root, "item", key=key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Loads XML data from a file and deserializes it to a Python dictionary.
    Args:
        filename: The name of the file from which to load the XML data.
    Returns:
        The Python dictionary deserialized from the XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for item in root.findall("item"):
        key = item.get("key")
        value = item.text
        result[key] = value
    return result

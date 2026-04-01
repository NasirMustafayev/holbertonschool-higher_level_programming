#!/usr/bin/python3
"""
Module 5-text_indentation
>>>text_indentation("Line 1. Line 2? Line 3: Line 4")
Line 1.

Line 2?

Line 3:

Line 4
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip = False

    for i in range(len(text)):
        if skip and ' ' in text[i]:
            continue
        if skip and ' ' not in text[i]:
            skip = False

        if text[i] in (".", "?", ":"):
            print(text[i], end="\n\n")
            skip = True
        else:
            print(text[i], end="")

#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip = False

    for i in range(len(text)):
        if skip and ' ' in text[i]:
            continue
        if skip and not ' ' in text[i]:
            skip = False
        
        if text[i] in (".", "?", ":"):
            print(text[i],end="\n\n")
            skip = True
        else:
            print(text[i], end="")

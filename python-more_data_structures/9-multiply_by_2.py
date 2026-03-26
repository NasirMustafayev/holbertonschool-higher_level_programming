#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    result = {}
    for k, v in a_dictionary.items():
        result[k] = v*2

    return result

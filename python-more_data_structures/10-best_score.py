#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    biggest = None

    for key in list(a_dictionary):
        if biggest is None or a_dictionary[biggest] < a_dictionary[key]:
            biggest = key

    return biggest

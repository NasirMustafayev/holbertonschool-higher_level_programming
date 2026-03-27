#!/usr/bin/python3

def roman_to_int(roman):
    if roman is None or type(roman) is not str:
        return 0

    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0

    for i in range(len(roman)):
        current = values[roman[i]]

        if i + 1 < len(roman) and current < values[roman[i + 1]]:
            result -= current   # subtractive case (IV, IX, XL...)
        else:
            result += current   # normal case

    return result

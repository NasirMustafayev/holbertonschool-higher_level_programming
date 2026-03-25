#!/usr/bin/python3

from unittest import result


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    result = []

    for i in range(len(my_list)):
        if i != idx:
            result.append(my_list[i])
    my_list[:] = result

    return result

#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc != 1:
        if argc == 0:
            print("0 arguments.")
        else:
            print("{} arguments:".format(argc), end="\n")
    else:
        print("{} argument:".format(argc), end="\n")

    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))

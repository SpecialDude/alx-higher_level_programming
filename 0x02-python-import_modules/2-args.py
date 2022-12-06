#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    length = len(args)

    if length == 0:
        end = 's.'
    elif length == 1:
        end = ':'
    else:
        end = 's:'

    print("{} argument{}".format(length, end))

    for i in range(length):
        print("{}: {}".format(i + 1, args[i]))

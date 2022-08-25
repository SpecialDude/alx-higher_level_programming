#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    l = len(args)

    if l == 0:
        end = 's.'
    elif l == 1:
        end = ':'
    else:
        end = 's:'

    print("{} argument{}".format(l, end))

    for i in range(l):
        print("{}: {}".format(i + 1, args[i]))

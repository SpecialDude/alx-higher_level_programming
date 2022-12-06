#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c = ord(c)
        if c > 96 and c < 123:
            c = c - 32
        print("{:c}".format(c), end="")
    print()

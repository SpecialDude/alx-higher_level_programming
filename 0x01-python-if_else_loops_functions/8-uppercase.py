#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            print(chr(ord(c) - 10), end="")
        else:
            print(c, end="")
    print()

uppercase("adetayo")

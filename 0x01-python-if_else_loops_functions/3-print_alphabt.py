#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if not (chr(i) ==  'e' or chr(i) == 'q'):
        print("{i:c}".format(i=i), end="")

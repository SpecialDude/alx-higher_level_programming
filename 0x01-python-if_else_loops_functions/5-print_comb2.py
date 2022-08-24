#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{i:d}".format(i=i))
    else:
        print("{i:02d}".format(i=i), end=", ")

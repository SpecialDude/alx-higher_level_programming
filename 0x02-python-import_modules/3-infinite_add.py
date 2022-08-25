#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    print(sum(map(int, args)))

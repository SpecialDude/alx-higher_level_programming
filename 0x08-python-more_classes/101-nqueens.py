#!/usr/bin/python3

"""
A program that solves the N queens problem
"""

import sys


def main():
    """Program entry point"""

    args = sys.argv[1:]

    if len(args) != 1:
        print("Usage: nqueens N")
        exit(1)

    if not args[0].isdigit():
        print("N must be a number")
        exit(1)

    n = int(args[0])

    if n < 4:
        print("N must be at least 4")
        exit(1)

if __name__ == "__main__":
    main()
    
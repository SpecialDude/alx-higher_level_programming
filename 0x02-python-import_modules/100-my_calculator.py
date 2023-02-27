#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(args[0])
    b = int(args[2])
    op = args[1]

    if op == '+':
        r = add(a, b)
    elif op == '-':
        r = sub(a, b)
    elif op == '*':
        r = mul(a, b)
    elif op == '/':
        r = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, r))

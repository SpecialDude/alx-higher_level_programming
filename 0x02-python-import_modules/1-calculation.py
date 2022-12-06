#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    ad = add(a, b)
    su = sub(a, b)
    mu = mul(a, b)
    di = div(a, b)

    print("{a} + {b} = {ad}\n{a} - {b} = {su}".format(a=a, b=b, ad=ad, su=su))
    print("{a} * {b} = {mu}\n{a} / {b} = {di}".format(a=a, b=b, mu=mu, di=di))

#!/usr/bin/python
import calculator_1 as calc

if __name__ == "__main__":
    a = 10
    b = 5

    ad = calc.add(a, b)
    su = calc.sub(a, b)
    mu = calc.mul(a, b)
    di = calc.div(a, b)

    print("{a} + {b} = {ad}\n{a} - {b} = {su}".format(a=a, b=b, ad=ad, su=su))
    print("{a} * {b} = {mu}\n{a} / {b} = {di}".format(a=a, b=b, mu=mu, di=di))

#!/usr/bin/env pypy


def is_dividable(a, b):
    if (a / b) * b == a:
        return True
    else:
        return False


def rm(a, b):
    """remove b from a"""
    if b == 1:
        return a
    else:
        while is_dividable(a, b):
            a /= b
        return a


def lexp(a):
    if a == 1:
        return 1
    else:
        r = a
        while r * a <= 20:
            r *= a
    return r

x = range(2, 21)

for i in range(19):
    b = x[i]
    for j in range(i + 1, 19):
        a = x[j]
        if is_dividable(a, b):
            x[j] = rm(a, b)
    x[i] = lexp(b)

print x

import operator
print reduce(operator.mul, x)

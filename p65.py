#!/usr/bin/env pypy

from fractions import gcd


def num(i):
    if i == 1:
        return 2
    elif (i - 2) % 3 == 1:
        return 2 * (i / 3)
    else:
        return 1


def fun(n):
    a, b = 1, 0  # a / b
    for i in range(n, 0, -1):
        a, b = b, a
        a += num(i) * b
        g = gcd(a, b)
        a, b = a / g, b / g
    return a, b


for i in range(1, 11):
    print fun(i)

a, b = fun(100)
print a
print sum(int(c) for c in str(a).strip('L'))

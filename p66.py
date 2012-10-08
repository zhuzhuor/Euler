#!/usr/bin/env pypy

from math import sqrt
from fractions import gcd


# from p64
def init(n):
    a0 = int(sqrt(n))
    return a0, (1, n, -a0)  # (x, y, z)


def step(x1, y1, z1):
    t = y1 - (z1 ** 2)
    assert t % x1 == 0  # why always divisible?
    x2 = t / x1
    y2 = y1
    a = (int(sqrt(y2)) - z1) / x2
    z2 = -z1 - a * x2

    return a, (x2, y2, z2)


def result(lis):
    a, b = 1, 0
    for x in lis[::-1]:
        a, b = b, a
        a += x * b
        g = gcd(a, b)
        a, b = a / g, b / g
    return (a, b)


# http://en.wikipedia.org/wiki/Pell's_equation
def compute(n):
    a0, (x, y, z) = init(n)
    s = [a0]
    yield result(s)
    while True:
        a, (x, y, z) = step(x, y, z)
        s.append(a)
        yield result(s)

max_x = 0
res_D = None
for D in range(2, 1001):
    if int(sqrt(D)) ** 2 == D:
        continue

    print D,
    gen = compute(D)
    while True:
        x, y = gen.next()
        if x ** 2 - D * (y ** 2) == 1:
            print x
            if x > max_x:
                max_x = x
                res_D = D
            break
print 'result', res_D, max_x

#!/usr/bin/env pypy

from math import sqrt


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


def period(n):
    a0, (x, y, z) = init(n)
    # print a0, (x, y, z)
    s = list()
    while True:
        a, (x, y, z) = step(x, y, z)
        # print a, (x, y, z)
        if (a, (x, y, z)) in s:
            break
        else:
            s.append((a, (x, y, z)))
    return len(s)


count = 0
for i in range(2, 10000 + 1):
    if int(sqrt(i)) == sqrt(i):
        continue
    if period(i) % 2:
        count += 1
print count

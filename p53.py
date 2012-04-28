#!/usr/bin/env pypy

from math import factorial

def comb(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)

num = 0
for n in range(1, 101):
    for r in range(n + 1):
        if comb(n, r) > 1000000:
            num += 1
print num

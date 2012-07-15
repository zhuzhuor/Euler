#!/usr/bin/env pypy


def satisfied(x):
    st = str(x)
    return x == sum([int(c) ** 5 for c in st])

total = 0
for i in range(2, 1000000):
    if satisfied(i):
        total += i
print total

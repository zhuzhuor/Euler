#!/usr/bin/env pypy

count = 0

n = 1  # numberator
d = 2  # denominator
for i in range(2, 1001):
    n, d = d, 2 * d + n
    # print n + d, '/', d
    if len(str(n + d)) > len(str(d)):
        count += 1

print count

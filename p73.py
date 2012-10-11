#!/usr/bin/env pypy

from fractions import gcd

num = 0
for d in range(2, 12001):
    start = d // 3 + 1
    end = d // 2
    if end * 2 == d:
        end -= 1
    for i in range(start, end + 1):
        if gcd(i, d) == 1:
            num += 1
print num

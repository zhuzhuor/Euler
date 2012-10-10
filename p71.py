#!/usr/bin/env pypy

from fractions import gcd

target_ratio = 3.0 / 7
# print target_ratio

max_ratio = 0
result_n = None
result_d = None

for d in range(1, 1000001):
    n = int(target_ratio * d)
    r = n * 1.0 / d
    if r > max_ratio and r < target_ratio:
        max_ratio = r
        g = gcd(d, n)
        result_n = n / g
        result_d = d / g
print result_n, result_d

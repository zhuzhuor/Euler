#!/usr/bin/env pypy

last_10 = 0
for i in range(1, 1001):
    last_10 += i ** i
    last_10 %= 10000000000
print last_10

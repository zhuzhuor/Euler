#!/usr/bin/env pypy


def digital_sum(x):
    s = 0
    for i in str(x):
        s += int(i)
    return s

max_sum = 0
for x in range(100):
    for y in range(100):
        s = digital_sum(x ** y)
        if s > max_sum:
            max_sum = s
print max_sum

#!/usr/bin/env pypy

n = 1
sum = n

for i in range(500):
    step = 2 * (i + 1)
    n += step
    sum += n
    for j in range(3):
        n += step
        sum += n
print sum

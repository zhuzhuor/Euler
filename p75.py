#!/usr/bin/env pypy

from math import sqrt

limit = 1500000
#limit = 50

num = [0] * (limit + 1)

for x in range(1, limit // 3 + 1):
    if x % 1000 == 0:
        print x

    for y in range(x, (limit - x) // 2 + 1):
        a = x ** 2 + y ** 2
        r = int(sqrt(a))
        if x + y + r > limit:
            break
        if r ** 2 == a:
            num[x + y + r] += 1

results = [i for i in range(1, limit + 1) if num[i] == 1]
print len(results)

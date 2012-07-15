#!/usr/bin/env pypy

fac = []
for i in range(10):
    r = 1
    for j in range(1, i + 1):
        r *= j
    fac.append(r)
fac = tuple(fac)  # const then

results = set()
for x in range(10, 1000000):
    res = sum(fac[int(c)] for c in str(x))
    if res == x:
        results.add(x)
print sum(results)

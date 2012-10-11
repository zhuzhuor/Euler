#!/usr/bin/env pypy

from math import factorial

fact = [None] * 10
for i in range(10):
    fact[i] = factorial(i)


def next(x):
    res = 0
    while x:
        d = x % 10
        res += fact[d]
        x /= 10
    return res


num = {
        1: 1,
        2: 1,
        40585: 1,
        145: 1,
        169: 3,
        363601: 3,
        1454: 3,
        871: 2,
        45361: 2,
        872: 2,
        45362: 2,
}


result = 0
for start in range(2, 1000001):
    if start in num:
        continue

    terms = [start]
    curr = start
    while True:
        curr = next(curr)
        if curr in num:
            remaining = num[curr]
            break
        else:
            terms.append(curr)
    l = len(terms)
    for i in range(l):
        num[terms[i]] = l - i + remaining
    if l + remaining == 60:
        result += 1

print result
#print 69, num[69]
#print 78, num[78]
#print 540, num[540]

#!/usr/bin/env pypy


def num_nth(n):
    total = 0
    for i in range(1, 10):
        if len(str(i ** n)) == n:
            total += 1
    return total

result = 0
n = 1
while 9 ** n >= 10 ** (n - 1):
    result += num_nth(n)
    n += 1
print result

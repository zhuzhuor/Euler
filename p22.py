#!/usr/bin/env pypy


with open('names.txt') as f:
    l = eval('[' + f.read() + ']')
l.sort()


def score(s):
    r = 0
    for c in s:
        r += ord(c) - ord('A') + 1
    return r

sum = 0
for i in range(len(l)):
    sum += score(l[i]) * (i + 1)
print sum

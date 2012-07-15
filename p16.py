#!/usr/bin/env pypy

s = str(2 ** 1000)

print sum([int(i) for i in s])

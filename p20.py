#!/usr/bin/env pypy

from operator import mul
s = str(reduce(mul, range(1, 101)))
print sum(int(i) for i in s)

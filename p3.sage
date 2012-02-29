#!/usr/bin/env sage

a = 600851475143
r = factor(a)
s = 0
for x, d in list(r):
    s += x
print x


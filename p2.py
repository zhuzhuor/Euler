#!/usr/bin/env pypy

a = 1
b = 2
s = b

while True:
    c = a + b
    if c > 4000000:
        break
    if c % 2 == 0:
        s += c
    a = b
    b = c

print s

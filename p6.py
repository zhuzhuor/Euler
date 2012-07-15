#!/usr/bin/env pypy

a = sum([i ** 2 for i in range(101)])
b = sum([i for i in range(101)])
print a - b ** 2

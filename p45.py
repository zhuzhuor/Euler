#!/usr/bin/env pypy

set_p = set()
for i in range(166, 100000):
    set_p.add(i * (3 * i - 1) / 2)

set_ph = set()
for i in range(144, 100000):
    x = i * (2 * i - 1)
    if x in set_p:
        set_ph.add(x)

for i in range(286, 200000):
    x = i * (i + 1) / 2
    if x in set_ph:
        print x
#print 'not found'

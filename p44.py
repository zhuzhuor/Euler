#!/usr/bin/env pypy

pant_numb = set()
for i in range(1, 10000):
    pant_numb.add(i * (3 * i - 1) / 2)

set_d = set()
for x in pant_numb:
    for y in pant_numb:
        if x == y:
            continue

        if x + y in pant_numb and abs(x - y) in pant_numb:
            set_d.add(abs(x - y))
print min(set_d)

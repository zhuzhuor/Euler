#!/usr/bin/env pypy

NUM = 6
#NUM = 3


def gen_set(deg):
    ret_set = set()
    n = 1
    while True:
        p = n * ((deg - 2) * n + 4 - deg) / 2
        if p > 10000:
            break
        # if p >= 1000:
        if p >= 1000 and p % 100 >= 10:
            ret_set.add(p)
        n += 1
    return frozenset(ret_set)

set_tri = gen_set(3)
set_squ = gen_set(4)
set_pen = gen_set(5)
set_hex = gen_set(6)
set_hep = gen_set(7)
set_oct = gen_set(8)
all_sets = frozenset([set_tri, set_squ, set_pen,
        set_hex, set_hep, set_oct][:NUM])


from itertools import product


def got_represented(numbs, sets):
    if len(numbs) == 0:
        return True
    n = numbs[0]
    for s in sets:
        if n in s:
            if got_represented(numbs[1:], sets - set([s])):
                return True
    return False

for portions in product(range(10, 100), repeat=NUM):
    numbers = [portions[0] * 100 + portions[1]]
    if numbers[0] not in set_tri:
        continue
    for i in range(1, NUM):
        numbers.append(portions[i] * 100 + portions[(i + 1) % NUM])
    if got_represented(numbers[1:], all_sets - set([set_tri])):
        print numbers, sum(numbers)
        break

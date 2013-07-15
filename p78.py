#!/usr/bin/env pypy

data = {}


def comp(total, minimal=1):
    assert minimal > 0
    # print 'enter', total, minimal
    if total // 2 < minimal:
        # print total, minimal, '=> 1'
        return 1

    if (total, minimal) in data:
        return data[(total, minimal)]

    result = 1
    for new_min in range(minimal, total // 2 + 1):
        result += comp(total - new_min, new_min)

    # save intermediate compuation results
    data[(total, minimal)] = result
    # print total, minimal, '=>', result
    return result

for i in range(1, 7):
    print i, comp(i)

i = 0
while True:
    i += 1
    if comp(i) % 1000000 == 0:
        print i
        break

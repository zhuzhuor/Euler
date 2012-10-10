#!/usr/bin/env pypy

from itertools import permutations as perm


def transform(lis):
    mat = []
    for i in range(5):
        row = [None] * 3
        row[0] = lis[i]
        row[1] = lis[i + 5]
        row[2] = lis[(i + 1) % 5 + 5]
        mat.append(row)
    # make it unique
    # starting from the lowest outer value
    lowest = 100
    position = None
    for i in range(5):
        if lowest > mat[i][0]:
            lowest = mat[i][0]
            position = i
    mat = mat[position:] + mat[:position]

    return mat


def is_gon(gon):
    s = sum(gon[0])
    for i in range(1, 5):
        if sum(gon[i]) != s:
            return False
    return True


result = 0
result_p = None
result_g = None
gen = perm(range(1, 11))
for p in gen:
    if 10 not in p[:5]:
        # make sure 16-digit
        continue
    g = transform(p)
    if is_gon(g):
        r = ''
        for i in range(5):
            for j in range(3):
                r += str(g[i][j])
        assert len(r) == 16
        if int(r) > result:
            result = int(r)
            result_p = p
            result_g = g
    else:
        continue
print result
print result_p
print result_g

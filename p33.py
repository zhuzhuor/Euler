#!/usr/bin/env pypy


def cancel(a, b):
    """cancel the common terms of a and b"""
    al, ar = "%02d" % a
    bl, br = "%02d" % b
    if al == br:
        al = ''
        br = ''
    if ar == bl:
        ar = ''
        bl = ''
    a = al + ar
    b = bl + br
    if a == '' or b == '' or a == '0' or b == '0':
        return None
    elif len(a) == 2:
        return None
    else:
        return float(a) / float(b)

for a in range(1, 100):
    for b in range(a + 1, 100):
        ret = cancel(a, b)
        if ret is not None and ret == float(a) / float(b):
            print a, b

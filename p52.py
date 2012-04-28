#!/usr/bin/env pypy

def satisfied(num, scale=[2,]):
    digits = list(str(num))
    digits.sort()
    for i in scale:
        new_digits = list(str(i * num))
        new_digits.sort()
        if digits != new_digits:
            return False
    return True

scales = [2, 3, 4, 5, 6]
n = 10000
while True:
    if satisfied(n, scales):
        print n
        break
    else:
        n += 1

#!/usr/bin/env sage


def num_primes(str_x, debug=False):
    num = 0

    if str_x[0] == '*':
        gen = range(1, 10)
    else:
        gen = range(10)

    for i in gen:
        c = str(i)
        x = str_x.replace('*', c)
        if int(x) in Primes():
            if debug:
                print x
            num += 1

    return num

from itertools import combinations

x = 100000
while True:
    x = next_prime(x)
    for i in range(1, len(str(x))):
        pos_gen = combinations(range(len(str(x))), i)
        for pos in pos_gen:
            lis_x = list(str(x))
            for j in pos:
                lis_x[j] = '*'
            str_x = ''.join(lis_x)
            if num_primes(str_x) == 8:
                print x, str_x
                num_primes(str_x, debug=True)
                import sys
                sys.exit()

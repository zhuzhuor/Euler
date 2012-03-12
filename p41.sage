def is_pandigital(x):
    st = str(x)
    ss = frozenset(st)
    for i in range(1, len(st) + 1):
        if str(i) not in ss:
            return False
    return True

#print is_pandigital(2143)

from itertools import permutations
for length in range(9, 0, -1):
    gen_str = reduce(lambda a, b: a + b, [str(i) for i in range(length, 0, -1)])
    print gen_str
    gen = permutations(gen_str, length)
    for t in gen:
        x = int(''.join(t))
        if x in Primes():
            print 'Found', x
            import sys
            sys.exit()

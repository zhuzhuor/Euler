# This file was *autogenerated* from the file p49.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_3 = Integer(3); _sage_const_1000 = Integer(1000); _sage_const_10000 = Integer(10000); _sage_const_4 = Integer(4)
from itertools import permutations, combinations

def prime_perms(a):
    r = set()
    s = str(a)
    gen = permutations(s, _sage_const_4 )
    for i in gen:
        b = int(''.join(i))
        if b in Primes():
            r.add(b)

    return r

checked_numb = set()


def check(n):
    global checked_numb
    if n in checked_numb:
        return False, None

    if '0' in str(n):
        return False, None

    set_primes = prime_perms(n)
    checked_numb |= set_primes
    if len(set_primes) < _sage_const_3 :
        return False, None

    gen = combinations(set_primes, _sage_const_3 )
    for l in gen:
        l = list(l)
        l.sort()
        a, b, c = l
        if b - a == c - b:
            return True, (str(a), str(b), str(c))
    return False, None


x = next_prime(_sage_const_1000 )
while x < _sage_const_10000 :
    passed, terms = check(x)
    if passed and '1487' not in terms:
        break
    else:
        x = next_prime(x)

print ''.join(terms)

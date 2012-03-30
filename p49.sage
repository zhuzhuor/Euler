from itertools import permutations, combinations

def prime_perms(a):
    r = set()
    s = str(a)
    gen = permutations(s, 4)
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
    if len(set_primes) < 3:
        return False, None

    gen = combinations(set_primes, 3)
    for l in gen:
        l = list(l)
        l.sort()
        a, b, c = l
        if b - a == c - b:
            return True, (str(a), str(b), str(c))
    return False, None


x = next_prime(1000)
while x < 10000:
    passed, terms = check(x)
    if passed and '1487' not in terms:
        break
    else:
        x = next_prime(x)

print ''.join(terms)

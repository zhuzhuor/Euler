def shift(x, bitlen):
    s = str(x)
    l = ['0'] * (bitlen - len(s)) + list(s)
    l.append(l.pop(0))
    return int(''.join(l))

def circular_prime(x):
    saved = x
    bit_len = len(str(x))
    all_primes = set()
    while x in Primes():
        all_primes.add(x)
        x = shift(x, bit_len)
        if x == saved:
            return True, all_primes
    return False, all_primes

import sys

i = 2
circular_prime_set = set([i])
while True:
    i = next_prime(i)
    if i >= 1000000:
        break
    if i in circular_prime_set:
        continue
    #sys.stdout.write("%d " % i)
    #sys.stdout.flush()
    is_prime, prime_set = circular_prime(i)
    if is_prime:
        circular_prime_set |= prime_set
#print circular_prime_set
print
print len(circular_prime_set)


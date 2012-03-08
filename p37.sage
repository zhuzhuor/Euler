def is_good(x):
    s = list(str(x))
    l = len(s)
    n = ''
    for i in range(l - 1):
        n += s[i]
        if int(n) not in Primes():
            return False
    n = ''
    for i in range(l - 1):
        n = s[l - i - 1] + n
        if int(n) not in Primes():
            return False
    return True

p = 11
results = set()
while True:
    p = next_prime(p)
    if is_good(p):
        results.add(p)
        print results
        if len(results) == 11:
            break
print results
print sum(results)

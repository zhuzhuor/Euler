start = 2
results = {}
while start < 1000:
    i = start

    num = 0
    prime_num = None

    total = 0
    prime_total = None

    added = set()
    prime_added = None

    while total + i < 1000000:
        num += 1
        added.add(i)
        total += i
        if total in Primes():
            prime_total = total
            prime_added = added
            prime_num = num
        i = next_prime(i)
    results[prime_num] = prime_total  # , prime_added)

    start = next_prime(start)

#print results
print max(results), results[max(results)]

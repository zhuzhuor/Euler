#!/usr/bin/env sage

cached_results = {}


def num_ways(total, bound, depth=0):
    assert total > 0
    if total == 1:
        return 0  # 1 is not prime

    if bound > total:
        bound = total

    if (total, bound) in cached_results:
        return cached_results[(total, bound)]

    if (bound < total):
        end = bound
    else:
        end = bound - 1

    number = 0
    term = 2
    while term <= end:
        result = num_ways(total - term, term, depth + 1)
        number += result
        # print '--' * (depth + 1), (total, bound), term, '->', result
        term = next_prime(term)
    if bound == total and total in Primes():
        number += 1
    cached_results[(total, bound)] = number

    return number

# print num_ways(3, 3)
# print cached_results
# print num_ways(10, 10)

i = 10
while True:
    if num_ways(i, i) > 5000:
        break
    else:
        i += 1
print i

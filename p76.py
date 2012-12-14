#!/usr/bin/env pypy

cached_results = {}


def num_ways(total, bound, depth=0):
    assert total > 0
    if total == 1:
        return 1

    if bound > total:
        bound = total

    if (total, bound) in cached_results:
        return cached_results[(total, bound)]

    if (bound < total):
        start = bound
    else:
        start = bound - 1

    number = 0
    for term in range(start, 0, -1):
        result = num_ways(total - term, term, depth + 1)
        number += result
        # print '--' * (depth + 1), (total, bound), term, '->', result
    if bound == total:
        number += 1
    cached_results[(total, bound)] = number

    return number

# print num_ways(2, 2) - 1
# print num_ways(3, 3) - 1
# print num_ways(2, 2) - 1
# print num_ways(4, 4) - 1
# print num_ways(5, 5) - 1
print num_ways(100, 100) - 1

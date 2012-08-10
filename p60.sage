UPPER_BOUND = 20000

list_primes = []
i = 2
while i < UPPER_BOUND:
    list_primes.append(i)
    i = next_prime(i)
print len(list_primes)


def check_pair(a, b):
    if int(str(a) + str(b)) not in Primes():
        return False
    if int(str(b) + str(a)) not in Primes():
        return False
    return True


from itertools import combinations as comb

# set of 2 elements
set_2 = set()
for x1, x2 in comb(list_primes, 2):
    if check_pair(x1, x2):
        set_2.add((x1, x2))
print len(set_2)


def higher_degree(in_set):
    out_set = set()
    for l1, l2 in comb(in_set, 2):
        diff = set(l1) - set(l2)
        if len(diff) == 1:
            x = diff.pop()
            diff = set(l2) - set(l1)
            y = diff.pop()
            t = tuple(sorted([x, y]))
            if t in set_2:
                out_set.add(tuple(sorted(list(l2) + [x])))
    return out_set

set_3 = higher_degree(set_2)
print len(set_3)

set_4 = higher_degree(set_3)
print len(set_4)

set_5 = higher_degree(set_4)
print 'set_5', len(set_5)

total = 1000000000000000
for t in set_5:
    s = sum(t)
    if s < total:
        total = s
        print s, t
print set_5

from itertools import permutations as perm

def get_num(lis):
    sum = 0
    num = len(lis)
    for i in range(num):
        sum += lis[i] * (10**(num - i - 1))
    return sum

results = set()

gen = perm(range(1, 10))
for tup in gen:
    for len1 in range(1, 5):
        x1 = get_num(tup[: len1])
        for len2 in range(1, 5):
            x2 = get_num(tup[len1 : len1 + len2])
            x3 = get_num(tup[len1 + len2 :])
            if x1 * x2 == x3:
                results.add(x3)
print results
print sum(results)


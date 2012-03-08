from itertools import permutations

def is_good(t, d):
    s = ''.join(t)
    a = int(s)
    for j in range(2, d + 1):
        s += str(j * a)
    if len(s) == 9 and len(set(s)) == 9 and '0' not in s:
        return True, int(s)
    else:
        return False, None

# print is_good(('1','9','2'), 3)

max_result = 0
for i in range(1, 5):
    gen = permutations('123456789', i)
    for x in gen:
        for j in range(2, 9 / i + 1):
            good, result = is_good(x, j)
            if good and max_result < result:
                # print x, j
                max_result = result
print max_result

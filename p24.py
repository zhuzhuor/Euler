from itertools import permutations as perm

a = perm(range(10))
for i in range(1000000):
    x = a.next()
print ''.join(str(i) for i in x)




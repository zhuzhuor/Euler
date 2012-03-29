def dividable(a, b):
    if (a / b) * b == a:
        return True
    else:
        return False


def is_good(s):
    if dividable(int(s[1:4]), 2)  and \
       dividable(int(s[2:5]), 3)  and \
       dividable(int(s[3:6]), 5)  and \
       dividable(int(s[4:7]), 7)  and \
       dividable(int(s[5:8]), 11) and \
       dividable(int(s[6:9]), 13) and \
       dividable(int(s[7:10]), 17):
        return True
    else:
        return False

from itertools import permutations as perm

all_good = []
gen = perm('0123456789', 10)
for l in gen:
    n = ''.join(l)
    if is_good(n):
        all_good.append(int(n))

print all_good
print sum(all_good)

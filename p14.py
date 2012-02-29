def get_next(x):
    if x % 2:
        return 3 * x + 1
    else:
        return x / 2

import sys

longest = 1
max_len = 1
for i in range(3, 1000000):
    if i % 10000 == 3:
        sys.stdout.write("%d " % i)
        sys.stdout.flush()

    n = i
    len = 2
    while True:
        # print n
        n = get_next(n)
        if n == 1:
            break
        else:
            len += 1

    if max_len < len:
        max_len = len
        longest = i

print
print longest



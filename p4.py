def is_plaindromic(x):
    return str(x) == str(x)[::-1]

max = 0
for a in range(1000):
    for b in range(1000):
        c = a * b
        if is_plaindromic(c) and max < c:
            max = c

print max

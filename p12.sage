i = 1
x = 1
while True:
    n = len(divisors(x))
    if n > 500:
        break
    i += 1
    x = i * (i + 1) / 2

print x

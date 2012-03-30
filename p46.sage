from math import sqrt

x = 9
while True:
    x += 2
    if x in Primes():
        continue

    passed = False
    for i in range(1, int(sqrt(x / 2)) + 1):
        if x - 2 * (i ** 2) in Primes():
            passed = True
            break
    if not passed:
        break
print x

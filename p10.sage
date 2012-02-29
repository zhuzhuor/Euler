s = 0
x = 1
while next_prime(x) < 2000000:
    x = next_prime(x)
    s += x
print s

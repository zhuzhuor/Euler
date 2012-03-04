def get_len(a, b):
    f = lambda x: x**2 + a*x + b
    i = 0
    while True:
        if f(i) not in Primes():
            break
        else:
            i += 1
    return i

max_len = 0
max_a = None
max_b = None
for a in range(-999, 1000):
#    print a,
    for b in range(2, 1000):
        if b not in Primes():
            continue
        this_len = get_len(a, b)
        if max_len < this_len:
            max_len = this_len
            max_a = a
            max_b = b
#print
print max_a * max_b

        


r = 0
n = 1
num_primes = 0
while True:
    r += 1
#for r in range(1, 5):
    for i in range(4):
        n += 2 * r
        if n in Primes():
            num_primes += 1
        #print n, num_primes
    if num_primes * 1.0 / (1 + 4 * r) < 0.1:
        break
print 2 * r + 1

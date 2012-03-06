def is_both(x):
    base2 =  bin(x)[2:]
    base10 = str(x)

    if base2 == base2[::-1] and base10 == base10[::-1]:
        return True
    else:
        return False

total = 0
for i in range(1000000):
    if is_both(i):
        total += i
print total

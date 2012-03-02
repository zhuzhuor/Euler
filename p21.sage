def sum_proper_divisors(x):
    return sum(divisors(x)[:-1])

num = [0] * 10000
for i in range(2, 10000):
    num[i] = sum_proper_divisors(i)

amicable_numbers = set()
for i in range(2, 10000):
    if num[i] < 10000 and i != num[i] and num[num[i]] == i: 
        amicable_numbers.add(i)

print amicable_numbers
print sum(amicable_numbers)

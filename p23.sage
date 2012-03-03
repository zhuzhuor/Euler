def is_abundant(x):
    return sum(divisors(x)[:-1]) > x

abundant_nums = set()
for i in range(1, 28123 + 1):
    if is_abundant(i):
        abundant_nums.add(i)

nums_written = set()
for x in abundant_nums:
    for y in abundant_nums:
        nums_written.add(x + y)

sum = 0
for i in range(1, 28123 + 1):
    if i not in nums_written:
        sum += i
print sum

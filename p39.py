def num_solutions(p):
    num = 0
    for a in range(1, p / 2):
        for b in range(a, p / 2):
            if a**2 + b**2 == (p - a - b)**2:
                num += 1
                #print a, b, p - a - b
    return num

max_num = 0
max_i = 0
for i in range(1, 1001):
    num = num_solutions(i)
    if max_num < num:
        max_num = num
        max_i   = i
print max_i


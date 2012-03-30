def get_factors(x):
    return frozenset([a for a, b in factor(x)])

i = 4
while True:
    #if i % 1000 == 0:
        #print i

    set_1 = get_factors(i)
    if len(set_1) != 4:
        i += 1
        continue

    set_2 = get_factors(i + 1)
    if len(set_2) != 4:
        i += 2
        continue
    if len(set_1 & set_2) != 0:
        i += 1
        continue

    set_3 = get_factors(i + 2)
    if len(set_3) != 4:
        i += 3
        continue
    if len(set_2 & set_3) != 0:
        i += 2
        continue

    set_4 = get_factors(i + 3)
    if len(set_4) != 4:
        i += 4
        continue
    if len(set_3 & set_4) != 0:
        i += 3
        continue

    break

print i

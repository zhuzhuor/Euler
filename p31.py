#!/usr/bin/env pypy

# import sys

num = 0
for n1 in range(200 / 1 + 1):
    # print n1,
    # sys.stdout.flush()

    s1 = n1
    for n2 in range(200 / 2 + 1):
        s2 = s1 + 2 * n2
        if s2 > 200:
            break
        for n5 in range(200 / 5 + 1):
            s5 = s2 + 5 * n5
            if s5 > 200:
                break
            for n10 in range(200 / 10 + 1):
                s10 = s5 + 10 * n10
                if s10 > 200:
                    break
                for n20 in range(200 / 20 + 1):
                    s20 = s10 + 20 * n20
                    if s20 > 200:
                        break
                    for n50 in range(200 / 50 + 1):
                        s50 = s20 + 50 * n50
                        if s50 > 200:
                            break
                        for n100 in range(200 / 100 + 1):
                            s100 = s50 + 100 * n100
                            if s100 > 200:
                                break
                            for n200 in range(200 / 200 + 1):
                                s200 = s100 + 200 * n200
                                if s200 == 200:
                                    num += 1
                                elif s200 > 200:
                                    break

# print
print num

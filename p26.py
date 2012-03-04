def len_recur(n):
    r = 1
    q_r_list = []
    while True:
        q = r / n
        r = r - q * n

        if q == 0 and r == 0:
            return 0

        if (q, r) in q_r_list:
            # print q_r_list + [(q, r)]
            for i in range(-1, -(len(q_r_list) + 1), -1):
                if (q, r) == q_r_list[i]:
                    return -i
        else:
            q_r_list.append((q, r))
            r *= 10

max_len = 0
max_n   = None
for i in range(2, 1000):
    l = len_recur(i)
    if max_len < l:
        max_len = l
        max_n = i
print max_n

max_result = 1
result_n = None
for n in range(2, 1000001):
    r = n * 1.0 / euler_phi(n)
    if r > max_result:
        max_result = r
        result_n = n
print result_n

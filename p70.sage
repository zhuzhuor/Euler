def is_permutation(a, b):
    sa = str(a)
    sb = str(b)

    if len(sa) != len(sb):
        return False

    if sorted(list(sa)) == sorted(list(sb)):
        return True
    else:
        return False


min_ratio = 10000000
result_n = None
for n in range(2, 10000000):
    if n % 100000 == 0:
        print n
    phi = euler_phi(n)
    if n * 1.0 / phi < min_ratio and is_permutation(phi, n):
        min_ratio = n * 1.0 / phi
        result_n = n
print result_n

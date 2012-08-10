FILE_NAME = 'primes.py'

with open(FILE_NAME, 'w') as f:
    f.write('#!/usr/bin/env pypy\n')


def write2file(name_var, list_primes):
    with open(FILE_NAME, 'a') as f:
        line = '\n\nlist_' + name_var + ' = (\n'
        f.write(line)
        line = ' ' * 4
        for p in list_primes:
            # 79 for pep8; 1 for the ending space to be removed
            if len(line) + len(str(p)) + 2 < 79 + 1:
                line += str(p) + ', '
            else:
                line = line[: -1] + '\n'  # remove the ending space
                f.write(line)
                line = ' ' * 4
        if line != ' ' * 4:
            line = line[: -2] + '\n'
            f.write(line)
        f.write(')\n')
        f.write('set_' + name_var + ' = frozenset(list_' + name_var + ')\n')


def primes_under(upper_bound):
    list_primes = []
    i = 2
    while i < upper_bound:
        list_primes.append(i)
        i = next_prime(i)
    return list_primes


write2file('primes_1000', primes_under(1000))
write2file('primes_10000', primes_under(10000))
write2file('primes_100000', primes_under(100000))
write2file('primes_1000000', primes_under(1000000))
write2file('primes_10000000', primes_under(10000000))
#write2file('primes_100000000', primes_under(100000000))


file_ending = """

if __name__ == '__main__':
    test = (2, 3, 4, 5, 6, 7, 8, 9, 10)
    for t in test:
        print t,
        print 'is' if t in set_primes_100000 else "isn't",
        print 'prime'
"""


with open(FILE_NAME, 'a') as f:
    f.write(file_ending)

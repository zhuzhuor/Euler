#!/usr/bin/env pypy


def is_palindromic(x):
    return str(x) == str(x)[::-1]

# print is_palindromic(221)


def is_lychrel(x):
    for i in range(50):
        x += int(str(x)[::-1])
        if is_palindromic(x):
            return False
    return True

count = 0
for i in range(10000):
    if is_lychrel(i):
        count += 1
print count

#!/usr/bin/env pypy

with open('cipher1.txt') as f:
    content = f.read()

cipher = ''
for i in content.split(','):
    cipher += chr(int(i))

from itertools import product
gen = product(range(97, 123), repeat=3)
for key in gen:
    plain = ''
    for i in range(len(cipher)):
        plain += chr(ord(cipher[i]) ^ key[i % 3])
    if ' is ' in plain and ' are ' in plain:
        break
print plain

sum = 0
for i in plain:
    sum += ord(i)
print sum

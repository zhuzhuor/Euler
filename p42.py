#!/usr/bin/env pypy

tri_numbers = []
for i in range(100):
    tri_numbers.append(i * (i + 1) / 2)
tri_numbers = frozenset(tri_numbers)


def val_word(w):
    val = 0
    for c in w.upper():
        val += ord(c) - 64
    return val

with open('words.txt') as f:
    text = f.read()
    list_words = eval(text)

# first time to write like this
# learnt from http://goo.gl/6tegs
print sum(val_word(w) in tri_numbers for w in list_words)

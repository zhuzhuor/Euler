#!/usr/bin/env pypy


num_lines = 0
data = []
with open('triangle.txt') as f:
    line = f.readline()
    while line:
        num_lines += 1
        row = [int(i) for i in line.split(' ')]
        data.append(row)
        line = f.readline()
print '#lines', num_lines


for r in range(num_lines - 1, 0, -1):  # from num_lines - 1 to 1
    for c in range(len(data[r]) - 1):
        if data[r][c] > data[r][c + 1]:
            data[r - 1][c] += data[r][c]
        else:
            data[r - 1][c] += data[r][c + 1]
print data[0][0]

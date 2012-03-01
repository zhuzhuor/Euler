num = [[None] * 21] * 21

def compute(x, y):
    if x == 0 or y == 0:
        return 1
    else:
        return num[x][y - 1] + num[x - 1][y]

for x in range(21):
    for y in range(21):
        num[x][y] = compute(x, y)

print num[20][20]

a = 1
b = 1
i = 2
while True:
    i += 1
    b, a = a + b, b
    if len(str(b)) == 1000:
        break

print i

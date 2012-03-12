s = ''
i = 1
while True:
    s += str(i)
    if len(s) < 1000000:
        i += 1
    else:
        break

print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])

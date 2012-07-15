#!/usr/bin/env pypy

below_20 = (
    None, 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
)

tens = (
    None, None, 'twenty', 'thirty', 'forty',
    'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
)


def english(x):
    assert x <= 1000
    if x == 1000:
        return 'one thousand'
    else:
        ret = ''
        if x >= 100:
            h = x / 100
            ret += below_20[h] + ' hundred'
            if x % 100 == 0:
                return ret
            else:
                ret += ' and '
        x %= 100
        if x <= 19:
            ret += (below_20[x])
        else:
            t = x / 10
            ret += tens[t]
            if x % 10 == 0:
                return ret
            else:
                x %= 10
                ret += '-' + below_20[x]
        return ret


def num(s):
    return len(s.replace(' ', '').replace('-', ''))

sum = 0
for i in range(1, 1001):
    words = english(i)
    sum += num(words)
print sum

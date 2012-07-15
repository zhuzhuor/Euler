#!/usr/bin/env pypy


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def num_days(year, month):
    assert month >= 1 and month <= 12
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month != 2:
        return 30
    else:
        if is_leap_year(year):
            return 29
        else:
            return 28


def total_num_days(year, month, day):
    total_num = 0
    for i in range(1900, year):
        if is_leap_year(i):
            total_num += 366
        else:
            total_num += 365
    for i in range(1, month):
        total_num += num_days(year, i)
    total_num += day - 1

    return total_num


def which_day(year, month, day):
    n = total_num_days(year, month, day) + 1
    return n % 7


count = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if 0 == which_day(y, m, 1):
            count += 1

print count

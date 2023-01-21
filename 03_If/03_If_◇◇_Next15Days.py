days_in_month = [31, -1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d, m, y = [int(e) for e in input().split()]
y -= 543
n = 31
if days_in_month[m-1] == 30:
    n = 30
else:
    if m == 2:
        n = 28
        if y % 400 == 0:
            n = 29
        if y % 4 and not y % 100:
            n = 29
d += 15
if d > n:
    d -= n
    m += 1
if m > 12:
    m -= 12
    y += 1
y += 543
print("{}/{}/{}".format(d, m, y))
a, b, c, d = [int(i) for i in input().split()]

if a > b:
    tmp = a
    a = b
    b = tmp
    
    if d >= a:
        if c > d:
            c -= a
    else:
        c += a
    b = a+c+d
else:
    if c > a and a >= b:
        d += a
    if d > c:
        b += 2
    else:
        b *= 2

print("{} {} {} {}".format(a, b, c, d))
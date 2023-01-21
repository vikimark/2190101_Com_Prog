a,b,c,d,e = [int(input()) for i in range(5)]

def swap(a, b):
    return [b, a]

if a > b:
    a,b = swap(a, b)
if c > d:
    c,d = swap(c,d)
if a > c:
    b,d=swap(b,d)
    c = a
a = e
if a > b:
    a,b=swap(a,b)
if c > a:
    b,d=swap(b,d)
    a=c
if a > d:
    print(d)
else:
    print(a)
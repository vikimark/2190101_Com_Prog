a=float(input())
steps = 0
b=a
while b > 0:
    steps+=1
    b=b//10

u=steps
l=0
x=((u+l)/2.)
while abs(a-10**x) > 10**-10*max(a, 10**x):
    if 10**x > a:
        u = x
    elif 10**x < a:
        l = x
    x = (u+l)/2.
print(round(x, 6))
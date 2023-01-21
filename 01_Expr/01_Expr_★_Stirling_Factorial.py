import math as m
a=m.exp
n=int(input())
t=(m.pi*2)**.5*n**(n+.5)
print(t*a(-n+1/(12*n+1)))
print(t*a(-n+1/(12*n)))
f=round
a,b,c=[float(input()) for _ in range(3)]
g=(b**2-(4*a*c))**0.5/(2*a)
h=-b/(2*a)
print(f(h-g,3),f(h+g,3))
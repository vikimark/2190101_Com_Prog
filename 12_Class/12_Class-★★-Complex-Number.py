class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b   = b
    def __str__(self):
        s = ""
        if self.a != 0:
            s+=str(self.a)+'+'
        if self.b != 0 and self.b != 1 and self.b > 0:
            s+=str(self.b)+'i'
        elif self.b != 0 and self.b == 1:
            s+='i'
        elif self.b != 0 and self.b == -1:
            s=s[:-1]
            s+="-i"
        elif self.b != 0 and self.b < 0:
            s=s[:-1]
            s+=str(self.b)+'i'
        elif self.b == 0 and self.a == 0:
            s+= str(0)
        else: s=s[:-1]
        return s
    def __add__(self, rhs):
        return Complex(self.a+rhs.a, self.b+rhs.b)
    def __mul__(self, rhs):
        return Complex(self.a*rhs.a-self.b*rhs.b, self.b*rhs.a+self.a*rhs.b)
    def __truediv__(self, rhs):
        a,b = self.a, self.b
        c,d = rhs.a, rhs.b
        real = (a*c+b*d)/(c**2+d**2)
        im = (-a*d+b*c)/(c**2+d**2)
        return Complex(real, im)


t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if  t==1        :   print(c1)
elif    t==2    :   print(c2)
elif    t==3    :   print(c1+c2)
elif    t==4    :   print(c1*c2)
else            :   print(c1/c2)
a,b,c=list(map(float,input()[1:-1].split(', ')))
d,e,f=list(map(float,input()[1:-1].split(', ')))
print('{} + [{}, {}, {}] = [{}, {}, {}]'.format(a,b,c,d,e,f,a+d,b+e,c+f))
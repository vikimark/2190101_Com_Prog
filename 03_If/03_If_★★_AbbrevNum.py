subfix = ['K', 'M', 'B']
n = input()
if len(n) <= 3:
    print(n)
elif len(n) > 3 and len(n) < 13:
    ndigit = (len(n)-1)//3
    isFloat = len(n) in [4, 7, 10]
    sub = subfix[ndigit-1]
    n = round(int(n), -(ndigit*3-1) if isFloat else -(ndigit*3))
    n = float(n) / (1000.**ndigit)
    if not isFloat:
        n = int(n)
    print("{}{}".format(n,sub))
else:
    print(str(round(int(n[0:-8]), -1))[:-1]+'B')
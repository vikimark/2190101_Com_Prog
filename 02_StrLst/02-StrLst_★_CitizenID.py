a=input()
print(a[0],a[1:5],a[5:10],a[-2:],(11-sum([(13-i)*int(a[i]) for i in range(12)])%11)%10)
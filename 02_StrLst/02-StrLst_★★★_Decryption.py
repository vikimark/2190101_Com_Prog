i=input()
d=str(int(i[3::7])+int(i[7::5])+10000)[-4:-1]
print(d+chr(sum(map(int,d))%10+65))
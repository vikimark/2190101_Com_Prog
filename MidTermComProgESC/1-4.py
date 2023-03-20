n=int(input())-1
s=input().split()
s[n]=s[n][::-1]
print(*s)
n=int(input())
ans = [n]
while n != 1:
    if n % 2 == 0:
        n = n/2
        ans.append(int(n))
    else: 
        n = 3*n + 1
        ans.append(int(n))

print(*ans[-15:],sep="->")

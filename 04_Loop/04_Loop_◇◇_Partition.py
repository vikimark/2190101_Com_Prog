d = [int(i) for i in input().split()]
p = d[-1]
i = -1 
j = 0
n = len(d)
while j < n-1:
    if d[j] <= p:
        i += 1
        tmp = d[i]
        d[i] = d[j]
        d[j] = tmp
    j+=1
tmp = d[i+1]
d[i+1] = d[-1]
d[-1] = tmp
print(d)


ans = []
count = 0
for i in range(int(input())):
    if i%2==0:
        ans.append(input())
    else:
        ans.insert(0, input())
    count+=1

a = input()
if a != '-1':
    for i, s in enumerate(a.split()):
        if count%2==0:
            ans.append(s)
        else:
            ans.insert(0, s)
        count+=1
    a=input()
    while a != '-1':
        if count%2==0:
            ans.append(a)
        else:
            ans.insert(0, a)
        count+=1
        a=input()

print(ans)
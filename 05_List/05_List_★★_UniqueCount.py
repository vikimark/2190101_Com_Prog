ans = []
sort = sorted(map(int, input().split()))
for i, a in enumerate(sort):
    if i==len(sort)-1:
        ans.append(a)
    elif a != sort[i+1]:
        ans.append(a)
print(len(ans),ans[:10],sep="\n")
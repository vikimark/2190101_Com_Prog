ans = {}
a = input()
while a != 'q':
    name, typ = a.split(', ')
    if typ not in ans:
        ans[typ] = [name]
    else:
        ans[typ].append(name)
    a=input()
for key, value in ans.items():
    print(key+': ',end='')
    print(*value,sep=', ')
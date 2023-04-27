infos = []
a = input()
while a != 'q':
    name, typ = a.split(', ')
    isIn = False
    for info in infos:
        t = info[0]
        if t == typ:
            isIn = True
            info[1].append(name)
            break
    if not isIn:
        infos.append([typ, [name]])
    a = input()
        
for info in infos:
    typ = info[0]
    print(typ,': ', sep='',end='')
    print(*info[1], sep=', ')
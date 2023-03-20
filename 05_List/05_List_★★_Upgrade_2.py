grades=['A','B+','B','C+','C','D+','D','F']
ids=[]
a = input()
while a != 'q':
    a = a.split()
    ids.append([int(a[0]), grades.index(a[1])])
    a = input()

for id in input().split():
    for info in ids:
        if int(id) == info[0]:
            info[1] = info[1]-1 if info[1] != 0 else info[1]
ids = sorted(ids, key=lambda x: x[0])


for info in ids:
    print(info[0], grades[info[1]])
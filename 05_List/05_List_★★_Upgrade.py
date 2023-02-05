grades=['A','B+','B','C+','C','D+','D','F']
ids=[]
a = input()
while a != 'q':
    a = a.split()
    ids.append(a[0])
    ids.append(grades.index(a[1]))
    a = input()

for id in input().split():
    ids[ids.index(id)+1] = ids[ids.index(id)+1]-1 if ids[ids.index(id)+1] > 0 else ids[ids.index(id)+1]

for i in range(0, len(ids), 2):
    print(ids[i], grades[ids[i+1]])
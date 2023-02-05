coors = []
for i in range(1, int(input())+1):
    x, y = map(float, input().split())
    coors.append([x, y, (x**2+y**2)**.5, i])
coors = sorted(coors, key=lambda x: x[2])
print("#{}: ({}, {})".format(coors[2][3], coors[2][0], coors[2][1]))
h1 = int(input())
m1 = int(input())
s1 = int(input())

h2 = int(input())
m2 = int(input())
s2 = int(input())

t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2

dt = t2 - t1
# print(dt)
dh = (dt // (60*60)) % 24
# print(dh)
dt -= dh * 60*60
# print(dt)
dm = (dt // 60) % 60
# print(dm)
dt -= dm*60
# print(dt)
ds = dt % 60
# print(ds)
print(str(dh)+":"+str(dm)+":"+str(ds))
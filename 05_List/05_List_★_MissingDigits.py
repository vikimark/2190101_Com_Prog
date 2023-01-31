n = [*range(9)]
for s in input():
    if s.isnumeric() and int(s) in n:
        n.remove(int(s))
if n:
    print(*n, sep=',')
else:
    print("None")
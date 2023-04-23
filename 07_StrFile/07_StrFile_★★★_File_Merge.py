filenmaes = input().split()
a = []
for filename in filenmaes:
    with open(filename) as f:
        contents = f.read().splitlines()
    for content in contents:
        id, score = content.split()
        a.append([id, score])

a.sort(key=lambda x: (x[0][-2:], x[0]))
for info in a:
    
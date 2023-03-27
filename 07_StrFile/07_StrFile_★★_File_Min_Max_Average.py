filename, year = input().split()
year = year[-2:]

with open(filename) as f:
    content = f.read().splitlines()

a = []
for info in content:
    id, score = info.split()
    if id[:2] == year:
        a.append(float(score))
if len(a) == 0:
    print("No data")
else: 
    print(min(a), max(a), sum(a)/len(a))
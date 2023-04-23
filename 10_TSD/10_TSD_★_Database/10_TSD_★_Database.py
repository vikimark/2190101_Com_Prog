fnames = [input() for _ in range(3)]
with open(fnames[0]) as f:
    courses = {s[0]:s[1] for s in [s.split(',') for s in [s.strip() for s in f.readlines()]]}
with open(fnames[1]) as f:
    teachers = {s[0]:s[1] for s in [s.split(',') for s in [s.strip() for s in f.readlines()]]}
with open(fnames[2]) as f:
    database = [s.split(',') for s in [s.strip() for s in f.readlines()]]
for value in database:
    if value[0] in courses and value[1] in teachers:
        print(courses[value[0]]+','+teachers[value[1]])
    else: print("record error")
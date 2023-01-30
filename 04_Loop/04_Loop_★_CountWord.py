import re

w=input()
count=0
for s in re.sub(r'[^a-zA-Z]', ' ', input()).split():
    if s==w:
        count+=1
print(count)
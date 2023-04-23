n=int(input())
win=set()
lose=set()
for _ in range(n):
    s=input().split()
    win.add(s[0])
    lose.add(s[1])

print(sorted(list(win.difference(lose))))
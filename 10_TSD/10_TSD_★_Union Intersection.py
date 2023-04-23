n=int(input())
s=[set(map(int, input().split())) for _ in range(n)]
print(len(set.union(*s)),len(set.intersection(*s)),sep="\n") if s else print(0,0,sep="\n")
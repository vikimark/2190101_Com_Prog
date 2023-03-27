rnames = dict()
nnames = dict()

for i in range(int(input())):
    rname, nname = input().split()
    rnames[rname] = nname
    nnames[nname] = rname

for i in range(int(input())):
    s = input()
    try:
        ans = rnames[s]
        print(ans)
    except:
        try:
            ans = nnames[s]
            print(ans)
        except:
            print("Not found")
names = [   'Robert','Dick',
            'William','Bill',
            'James','Jim',
            "John","Jack",
            "Margaret","Peggy",
            'Edward','Ed',
            "Sarah","Sally",
            'Andrew','Andy',
            'Anthony','Tony',
            'Deborah','Debbie']
ans = []
for i in range(int(input())):
    s = input()
    if s in names:
        ind =  names.index(s)
        if ind % 2 == 0: # left
            ans.append(names[ind+1])
        else:
            ans.append(names[ind-1])
    else:
        ans.append("Not found")

print(*ans, sep="\n")
from P3_09_BNK48_testcase import testcase

def election(test):
    infos = []
    ans = []
    a = test.pop(0)
    while not a.isnumeric():
        infos.append(a.split())
        a = test.pop(0)
    
    if a == '1':
        candidate = {}
        for info in infos:
            voter, candid, score = info
            score = int(score)
            if candid not in candidate:
                candidate[candid] = score
            else:
                candidate[candid] += score
        high_score = sorted(candidate, key=lambda x:candidate[x], reverse=True)[:3]
        ans.append(", ".join(high_score))
    elif a == '2':
        candidate = {}
        for info in infos:
            voter, candid, score = info
            score = int(score)
            if candid not in candidate:
                candidate[candid] = set()
                candidate[candid].add(voter)
            else:
                candidate[candid].add(voter)
        print(candidate)
        high_score = sorted(candidate, key=lambda x:len(candidate[x]), reverse=True)[:3]
        ans.append(", ".join(high_score))
    elif a == '3':
        
    return ans

for i, test in enumerate(testcase):
    ans = election(test[0])
    print("Test: {} --> ".format(i+1), end="")
    assert test[1]==ans, ans
    print("Passed")
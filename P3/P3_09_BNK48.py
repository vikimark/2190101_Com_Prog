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
        high_score = sorted(candidate, key=lambda x:len(candidate[x]), reverse=True)[:3]
        ans.append(", ".join(high_score))
    elif a == '3':
        voters = {}
        for info in infos:
            voter, candid, score = info
            score = int(score)
            if voter not in voters:
                voters[voter] = {candid:score}
            elif candid not in voters[voter]:
                voters[voter][candid] = score
            else:
                voters[voter][candid] += score
        high_score = {}
        for _, candid in voters.items():
            candid = sorted(sorted(candid), key=lambda x:candid[x], reverse=True)[0]
            if candid not in high_score:
                high_score[candid] = 1
            else:
                high_score[candid] += 1
        ans.append(", ".join(sorted(sorted(high_score), key=lambda x:high_score[x], reverse=True)[:3]))
    return ans

for i, test in enumerate(testcase):
    ans = election(test[0])
    print("Test: {} --> ".format(i+1), end="")
    assert test[1]==ans, ans
    print("Passed")
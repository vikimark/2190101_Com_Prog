from P3_08_Bidding_test import testcase

def bidding(test):
    n = int(test.pop(0)) #first input
    items = {}
    bidders = []
    for _ in range(n):
        action = test.pop(0).split()
        if action[0] == "B":
            bid,itm = action[1:3]
            price = int(action[3])
            if bid not in bidders:
                bidders.append(bid)
            if itm not in items:
                items[itm] = [[bid, price]]
            else:
                items[itm].append([bid, price])
        if action[0] == "W":
            bid, itm = action[1:]
            if itm in items:
                for i in range(len(items[itm])-1, -1, -1):
                    if items[itm][i][0] == bid:
                        items[itm].pop(i)

    ans=[]
    for key in items:
        items[key].sort(key=lambda x: x[1], reverse=True)
    bidders = sorted(bidders)
    for bid in bidders:
        rcv_itm = []
        sum_price = 0
        for itm, info in items.items():
            if info:
                rcv_bid, price = info[0]
                if bid == rcv_bid:
                    rcv_itm.append(itm)
                    sum_price += price
        if rcv_itm:
            ans.append("{}: ${} -> {}".format(bid, sum_price, " ".join(sorted(rcv_itm))))
        else:
            ans.append("{}: ${}".format(bid, sum_price))
    
    return ans

for i, test in enumerate(testcase):
    ans = bidding(test[0])
    print("Test: {} --> ".format(i+1), end="")
    assert test[1]==ans, ans
    print("Passed")

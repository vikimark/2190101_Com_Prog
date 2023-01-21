from datetime import datetime, timedelta
import math

# testcase = [[[  "1 1 2559 1 1 2560"],
#             [   "366 -0.52 0.43 0.54"]],

#             [[  "1 1 2560 1 1 2561"],
#             [   "365 -0.73 0.22 0.37"]],
            
#             [[  "20 11 2540 10 2 2544"],
#             [   "1177 0.89 0.22 -0.87"]],
            
#             [[  "10 8 2541 27 10 2559"],
#             [   "6649 0.52 0.22 0.10"]]]

# def bio(test):
#     bd, bm, by, d, m, y = [int(e) for e in test.pop(0).split()]
#     by -= 543
#     y -= 543
#     blue_period = datetime(by, 12, 31) - datetime(by, bm, bd) + timedelta(days=1)
#     red_period = datetime(y, m, d) - datetime(y, 1, 1)
#     t=blue_period.days + (y-by-1)*365 + red_period.days
#     ans=[]
#     ans.append("{} {:.2f} {:.2f} {:.2f}".format(t, math.sin((2*math.pi*t)/23.), math.sin((2*math.pi*t)/28.), math.sin((2*math.pi*t)/33.)))
#     return ans

# for i, test in enumerate(testcase):
#     print("Test {} --> ".format(i), end="")
#     ans=bio(test[0])
#     assert test[1]==ans, ans
#     print("passed")

bd, bm, by, d, m, y = [int(e) for e in input().split()]
by -= 543
y -= 543
blue_period = datetime(by, 12, 31) - datetime(by, bm, bd) + timedelta(days=1)
red_period = datetime(y, m, d) - datetime(y, 1, 1)
t=blue_period.days + (y-by-1)*365 + red_period.days
ans=[]
ans.append("{} {:.2f} {:.2f} {:.2f}".format(t, math.sin((2*math.pi*t)/23.), math.sin((2*math.pi*t)/28.), math.sin((2*math.pi*t)/33.)))
for a in ans:
    print(a)
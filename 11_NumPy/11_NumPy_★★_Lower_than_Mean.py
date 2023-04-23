import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    scores = data[:, 1:].dot(weight[..., np.newaxis])
    ans = data[(scores < scores.mean()).flatten()][:, 0]
    if ans.size == 0:
        print("None")
    else:
        print(*ans, sep=", ")
exec(input().strip())
"""
w, d = read_data(); print(report_lower_than_mean(w,d))
0.3 0.5 0.2
5
610111 80 90 70
610222 50 80 68
610333 70 85 80
610444 60 50 90
610555 90 74 70

w, d = read_data(); print(report_lower_than_mean(w,d))
0.3 0.5 0.2
2
610111 80 90 80
610222 90 80 90
"""


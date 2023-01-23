scores = [float(i) for i in input().split()]
min = scores[0]
max = scores[0]
sum = 0.

for i, value in enumerate(scores):
    if min > value:
        min = value
    if max < value:
        max = value
    sum += value
sum = (sum - min - max)/2.
print(round(sum, 2))
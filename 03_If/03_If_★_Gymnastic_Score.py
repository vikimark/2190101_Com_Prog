scores = [float(i) for i in input().split()]
min = scores[0]
max = scores[0]
min_ind = 0
max_ind = 0
sum = 0.

for i, value in enumerate(scores):
    if min > value:
        min = value
        min_ind = i
    if max < value:
        max = value
        max_ind = i
    sum += value
sum = round(sum, 5)
sum = (sum - scores[min_ind] - scores[max_ind])/2.
print(sum)
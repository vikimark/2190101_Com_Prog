sum = 0.
length = 0
a = input()
while a != 'q':
    sum += float(a)
    length += 1
    a = input()

print(round(sum/length, 2))
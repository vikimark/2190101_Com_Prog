sum = 0.
length = 0
a = input()
if a == 'q':
    print("No Data")
else:
    while a != 'q':
        sum += float(a)
        length += 1
        a = input()

    print(round(sum/length, 2))
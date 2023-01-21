def isLeapYear(y):
    return y % 400 == 0 or (y % 4 == 0 and not y % 100 == 0)

d = int(input())
m = int(input())
y = int(input()) - 543

days_of_month = [31, 29 if isLeapYear(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_days = 0
for i in range(m-1):
    sum_days += days_of_month[i]
print(sum_days+d)
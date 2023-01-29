# testcase = [[[  "4 2",
#                 "               ",
#                 "  | |_|   | |_|",
#                 "  |   |   |   |",
#                 "       ",
#                 "|_|   |",
#                 "  |   |"]]]

# test = testcase[0][0]
number = [' _ | ||_|','     |  |',' _  _||_ ',' _  _| _|','   |_|  |',' _ |_  _|',' _ |_ |_|',' _   |  |',' _ |_||_|',' _ |_| _|']
a, b = [int(i) for i in input().split()]
numa = ['' for _ in range(a)]
numb = ['' for _ in range(b)]
for _ in range(3):
    temp = input()
    for x in range(0, a):
        numa[x] += temp[x*4:x*4+3]
for _ in range(3):
    temp = input()
    for x in range(0, b):
        numb[x] += temp[x*4:x*4+3]
x1, x2  = '', ''
for i in numa:
    x1 += str(number.index(i))        
for i in numb:
    x2 += str(number.index(i))
print(int(x1)+int(x2))

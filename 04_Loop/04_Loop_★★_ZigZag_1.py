maxZigZag, maxZagZig = -9999, -9999
minZigZag, minZagZig = 9999, 9999

for i in range(int(input())):
    x, y = [int(j) for j in input().split()]
    
    # zig-zag case
    if i%2 == 0: # min, max
        if minZigZag > x:
            minZigZag = x
        if maxZigZag < y:
            maxZigZag = y
    else: # max, min
        if minZigZag > y:
            minZigZag = y
        if maxZigZag < x:
            maxZigZag = x

    # zag-zig case
    if i%2 == 0: # max, min
        if minZagZig > y:
            minZagZig = y
        if maxZagZig < x:
            maxZagZig = x 
    else: # min, max
        if minZagZig > x:
            minZagZig = x
        if maxZagZig < y:
            maxZagZig = y

if input() == 'Zig-Zag':
    print(minZigZag, maxZigZag)
else: print(minZagZig, maxZagZig)

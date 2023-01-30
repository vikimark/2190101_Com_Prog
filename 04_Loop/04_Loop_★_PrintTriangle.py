a = int(input())
for i in range(1,a+1):
    if i != 1 and i != a:
        print(" "*(a-i),end="")
        print("*",end="")
        print(" "*(i*2-3),end="")
        print("*",end="")
        print(" "*(a-i))
    elif i == 1:
        print(" "*(a-i),end="")
        print("*",end="")
        print(" "*(a-i))
    else: print("*"*(a*2-1))
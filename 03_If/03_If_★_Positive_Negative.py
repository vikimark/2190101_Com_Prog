n = int(input())
if n == 0:
    print("zero")
    print("even")
else:
    print("positive") if n > 0 else print("negative")
    print("even") if n % 2 == 0 else print("odd")
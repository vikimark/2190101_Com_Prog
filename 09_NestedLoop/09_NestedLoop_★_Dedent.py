for _ in range(int(input())):
    s=input()
    if s.startswith('.'):
        count = 1
        while s[count] == '.':
            count+=1
        print(s[count//2:])
    else:print(s)
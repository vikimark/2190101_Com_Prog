p_ch = ''
sum = 0
sen = input()

for i, ch in enumerate(sen):
    if i == 0:
        print(ch, end=" ")
        sum = 1
        p_ch = ch
    elif i == len(sen)-1:
        if p_ch != ch:
            print(sum, end=" ")
            print(ch, end=" ")
            sum = 0
        sum += 1
        print(sum)
    elif p_ch != ch:
        print(sum, end=" ")
        print(ch, end=" ")
        p_ch = ch
        sum = 1
    else:
        sum+=1

    if len(sen)-1 == 0:
        print(sum)

cards = input().split()
for ch in input():
    if ch == 'C':
        cards = [*cards[len(cards)//2:], *cards[0:len(cards)//2], ]
        # tmp = cards[0:len(cards)/2].extend(cards[len(cards)/2])
    if ch == 'S':
        tmp = []
        for i in range(len(cards)//2):
            tmp.extend([cards[i], cards[i+len(cards)//2]])
        cards = tmp
        # cards = [[cards[i], cards[i+len(cards)/2]] for i in range(len(cards)/2)]
print(*cards)
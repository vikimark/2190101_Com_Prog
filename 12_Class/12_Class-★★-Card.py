class Card:
    def __init__(self, value, suit):
        self.symVal = value
        if value == 'A':
            self.value = 1
        elif value in ['J', 'Q', 'K']:
            self.value = 10 + ['0', 'J', 'Q', 'K'].index(value)
        else: self.value = int(value)
        self.suit = suit
        if suit == 'club':
            self.suitVal = 1
        elif suit == 'diamond':
            self.suitVal = 2
        elif suit == 'heart':
            self.suitVal = 3
        elif suit == 'spade':
            self.suitVal = 4
    def __str__(self):
        return '({} {})'.format(self.symVal, self.suit)
    def getScore(self):
        return min(self.value, 10)
    def sum(self, other):
        return (min(self.value, 10) + min(other.value, 10))%10
    def __lt__(self, rhs):
        tmpValueLHS = self.value
        tmpValueRHS = rhs.value
        if tmpValueLHS in [1, 2]:
            tmpValueLHS += 13
        if tmpValueRHS in [1, 2]:
            tmpValueRHS += 13
        return self.suitVal < rhs.suitVal if tmpValueLHS == tmpValueRHS else tmpValueLHS < tmpValueRHS

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])
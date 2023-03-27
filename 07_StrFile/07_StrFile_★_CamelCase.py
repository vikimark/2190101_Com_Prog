s = [c for c in input().replace('(',' ').replace(')',' ').replace('.',' ').replace('-',' ').replace(';',' ').replace('\"',' ').replace('>',' ').split()]
ans = ""
for i, word in enumerate(s):
    if i > 0:
        word = word[0].upper() + word[1:].lower()
    else:
        word = word.lower()
    ans+=word

print(ans)
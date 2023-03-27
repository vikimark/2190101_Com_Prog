s=""
a = []
c = []
while s != 'end':
    s = input()
    a.append(s)
a.pop()
for b in a:
    ans = ""
    for ch in b:
        if ch.isalpha() and ord('A')<=ord(ch)<=ord('Z'):
            ans += chr(((ord(ch) - ord('A')) + 13)%26 + ord('A'))
        elif ch.isalpha() and ord('a')<=ord(ch)<=ord('z'):
            ans += chr(((ord(ch) - ord('a')) + 13)%26 + ord('a'))
        else:
            ans += ch
    c.append(ans)
print(*c, sep='\n')
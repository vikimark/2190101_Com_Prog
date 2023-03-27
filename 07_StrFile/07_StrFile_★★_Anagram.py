a = input().lower().replace(' ', '')
b = input().lower().replace(' ', '')
print("YES" if sorted(a)==sorted(b) else "NO")
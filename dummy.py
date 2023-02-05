word = input()
n = input()
checker = ""
for i in n:
    if 96<ord(i.lower())<123:
        checker += i
    else:
        checker += " "
print(checker.split().count(word))

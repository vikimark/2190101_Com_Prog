ans=input()
test=input()
score_counter = 0
if len(ans) == len(test):
    for i, ch in enumerate(ans):
        if ch == test[i]:
            score_counter += 1
    print(score_counter)
else: print("Incomplete answer")
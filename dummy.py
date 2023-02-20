sol=input()
answers=[]
n=int(input())
def read_answers():
  for k in range(n):
    sid,ans=input().split()
    answers.append([sid,ans])
  return answers
def marking(ans,sol):
  score=0
  for i in range(len(ans)):
    if ans[i]==sol[i]:
      score+=1
  return score
def grading(score):
  g=[[80,'A'],[70,'B'],[60,'C'],[50,'D']]
  for a,b in g:
    if score>=a:
      return b
  return 'F'
def scoring(score,sol):
  scores=[]
  for id,ans in answers:
    score=marking(ans,sol)
    grade=grading(score)
    scores.append([id,score,grade])
  return scores
def report(scores):
  for id,sc,grade in scores:
    print(id,sc,grade)
def sort(scores):
  x=[]
  for id,score,grade in scores:
    x.append([score,id,grade])
    x.sort(reverse=True)
    for i in range(len(x)):
      scores[i]=[x[i][1],x[i][0],x[i][2]]
pt=[]
gr=[]
scores=[]
read_answers()
for k in range(n):
  pt.append(marking(answers[k][1],sol)/len(sol)*100)
for k in range(n):
  gr.append(grading(pt[k]))
for k in range(n):
  scores.append([answers[k][0],pt[k],gr[k]])
sort(scores)
report(scores)
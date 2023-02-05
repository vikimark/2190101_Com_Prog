q = list()
n = int(input())
t = list()
ticket = 0
c_call = 0
p_time = 0
for k in range(n):
    c = input().split()
    if c[0] == 'reset':
        ticket = int(c[1])
    elif c[0] == 'new':
        print("ticket", ticket)
        q.append([ticket, int(c[1])])
        ticket+=1
    elif c[0] == 'next':
        c_call = q[0][0]
        p_time = q[0][1]
        print("call", q.pop(0)[0])
    elif c[0] == 'order':
        t.append(int(c[1]) - p_time)
        print("qtime", c_call, t[-1])
    elif c[0] == 'avg_qtime':
        print("avq_qtime", round(sum(t)/len(t), 4))
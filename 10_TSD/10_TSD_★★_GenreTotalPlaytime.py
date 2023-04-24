from datetime import datetime, timedelta
genres = {}
for _ in range(int(input())):
    _,_,gen,time=input().split(', ')
    if gen not in genres:
        t=datetime.strptime(time, '%H:%M')
        genres[gen]=timedelta(hours=t.hour,minutes=t.minute)
    else:
        t=datetime.strptime(time, '%H:%M')
        genres[gen]+=timedelta(hours=t.hour,minutes=t.minute)
list_genres = [[k,t] for k,t in genres.items()]
list_genres = sorted(list_genres, key=lambda x:x[1], reverse=True)
mlen = min(3, len(list_genres))
for i in range(mlen):
    seconds = list_genres[i][1].total_seconds()
    result = '%d:%02d' % (seconds / 3600, seconds / 60 % 60)
    print(list_genres[i][0],result,sep=" --> ")
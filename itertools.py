import itertools

for i in itertools.count(1000,500):
    if i==5005000:
        break
    else:
        print(i,end=" ")
count=0
for i in itertools.cycle('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    if count>(15*26)-1:
        break
    else:
        print(i, end=" ")
        count+=1
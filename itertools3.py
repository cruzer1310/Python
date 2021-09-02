import itertools

count = 0
for i in itertools.count(1000,500):
        if count>3:
            break
        else:
            print(i,end=" ")
            count+=1

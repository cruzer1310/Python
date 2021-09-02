mx=101.00
S=[]
final=[]
for _ in range(int(input())):
    A=[]
    name = input()
    A.append(name)
    score = float(input())
    A.append(score)
    S.append(A)
    if(score<mx):
        smax=mx
        mx=score 
    elif(score>mx and score<smax):
        smax=score
        #print("new seconfd maax=",smax)
    else:
        continue

for x in range(0,len(S)):
    if(smax in S[x]):
        final.append(S[x][0])
    else:
        continue
final.sort()
for i in final:
    print(i)


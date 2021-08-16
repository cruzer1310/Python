k=31
o=""
while(True):
    r=k%16
    if(r<=9):
        o=o+str(r)
    elif(r==10):
        o=o+"A"
    elif(r==11):
        o=o+"B"
    elif(r==12):
        o=o+"C"
    elif(r==13):
        o=o+"D"
    elif(r==14):
        o=o+"E"
    else:
        o=o+"F"

    k=int(k/16)
    if(k==0):
        break
ans = o[::-1]
print(ans)
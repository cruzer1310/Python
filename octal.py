k=15
o=""
while(True):
    r=k%8
    o=o+str(r)
    k=int(k/8)
    if(k==0):
        break
ans = o[::-1]
print(ans)
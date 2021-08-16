k=8
o=""
while(True):
    r=k%2
    o=o+str(r)
    k=int(k/2)
    if(k==0):
        break
ans = o[::-1]
print(ans)
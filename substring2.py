def ss(s,pos,count):
    for x in range(pos+1,len(s)+1):
        count+=1
    return(count) 

vovel = ["A","E","I","O","U"]

nv=ns=0
s= "BANANA"
for x in range(len(s)):
    if(s[x] in vovel):
        nv=(ss(s,x,nv))
    else:
        ns = (ss(s,x,ns))
        
print (ns)
print (nv)
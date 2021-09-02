vovel = ["A","E","I","O","U"]
string="BANANA"
nv=ns=0
for x in range(len(string)):
    
    if(string[x] in vovel):
        nv=nv+(len(string)-x)
        #for i in range(x+1,len(string)+1):
        #    nv+=1
        #nv=(ss(string,x,nv))
    else:
        ns=ns+(len(string)-x)
        #for i in range(x+1,len(string)+1):
        #    ns+=1
        #        #    ns = (ss(string,x,ns))

if(ns>nv):
    print("Stuart",ns)
elif(nv>ns):
    print("Kevin",nv)
else:
    print("Draw")
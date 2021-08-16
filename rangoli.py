x=int(input())
r=2*x-1
width=2*r-1
for i in range(1,r+1):
    if(i<=(r+1)/2):
        s=i*2-1
    else:
        s=2*(r-i)+1
    count=x
    col=[]
    
    for m in range(1,s+1):
        
        col.append(chr(96+count))
        if (m<(s+1)//2):
            count-=1
        else:
            count+=1
    print(("-".join(col)).center(width,"-"))
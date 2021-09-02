x = int(input())
y = int(input())
z = int(input())
n = int(input())
A = []

C = []
for i in range(0,x+1):
    
    for j in range(0,y+1):
        
        for k in range(0,z+1):
            if(i+j+k==n):
                continue
            A=[i,j,k]
            C.append(A)
           # print (A)
        
       

print(C)
            
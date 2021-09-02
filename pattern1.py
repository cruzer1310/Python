arr = input().split() #first input odd number second input=first*3 ex:7,21 
n=int(arr[0])
m=int(arr[1])
s=".|."
for i in range(n):
    #print("****************    : "+ str(i))
    if (i<((n-1)/2)):
        #print("not hello")
        print((s*(i*2+1)).center(m,"-"))
    elif(i>((n-1)/2)):
        #print("hello")
        print((s*((n-i)*2-1)).center(m,"-"))
    else:
        print("WELCOME".center(m,"-"))
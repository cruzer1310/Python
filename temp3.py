def convert(base,i):
    k=i+1
    o=""
    ans=""
    if base==8:
        while(True):
            r=k%8
            o=o+str(r)
            k=int(k/8)
            if(k==0):
                break
    elif base==16:
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
    else:
        while(True):
            r=k%2
            o=o+str(r)
            k=int(k/2)
            if(k==0):
                break

    return (o[::-1])

n = int(input())
w=0
if n<2:
    w=2
elif n>=2 and n<4:
    w=3
elif n>=4 and n<8:
    w=4
elif n>=8 and n<16:
    w=5
elif n>=16 and n<32:
    w=6
elif n>=32 and n<64:
    w=7
else:
    w=8
for i in range(n):
    print(str(i+1).rjust(w-1),end="")
    print(convert(8,i).rjust(w),end="") #ocatal values
    print(convert(16,i).rjust(w),end="") #hexa values
    print(convert(2,i).rjust(w))  #binary values

    

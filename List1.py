N = int(input())
c= list()
l =list()
ip=list()
for _ in range(N):
    ip.clear()
    ip= input().split()
    #print(ip[0])
    if((ip[0]).lower()=="print"):
        print(l)
    elif((ip[0]).lower()=="insert"):
        l.insert(int(ip[1]),int(ip[2]))
    elif((ip[0]).lower()=="append"):
        l.append(int(ip[1]))
    elif((ip[0]).lower()=="sort"):
        l.sort()
    elif((ip[0]).lower()=="reverse"):
        l.reverse()
    elif((ip[0]).lower()=="pop"):
        l.pop()
    elif((ip[0]).lower()=="remove"):
        l.remove(int(ip[1]))
    else:
        continue

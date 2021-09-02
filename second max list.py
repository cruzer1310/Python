n = int(input())
arr = map(int, input().split())
mx=-101
smax=-101
for item in arr:
    #print(item)
    if(item>mx):
        smax=mx
        mx=item 
    elif(item<mx and item>smax):
        smax=item
        #print("new seconfd maax=",smax)
    else:
        continue


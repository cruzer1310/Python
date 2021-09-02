c = "helelo"
temp ="e"
count =0
start=0
last=len(c)
#i=0
while(c.find(temp,start,last)!=-1 ):
    count=count+1
    start=(c.find(temp,start,last))+1
    #print(f"{temp} found at position :{c.find(temp)}")
    #print(f"value of start now: {start}")
    if(start>last):
        break
    #i=i+1
print(f"Final count : {count}")
#print(c.find(temp))
#print(i)


string = "AABCAAADA"
k=3
final=temp=[]
for i in range(1,len(string)+1):
    #print(i)
    if string[i-1] not in temp:
            temp.append(string[i-1])
    if i%k==0:
        
        print("".join(temp))
        #final.append(temp)
        temp.clear()
    
#print(final)
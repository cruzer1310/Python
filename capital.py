n="hello 4am"
temp=n.split(" ")
print(len(temp))
m=""
for x in range(len(temp)):
    if not x==0:
        m+=" "
    if (temp[x].isalnum()==True and not (temp[x].isalpha()) ):
        m+=temp[x]
    else:
        m+=temp[x].capitalize()

print(m)
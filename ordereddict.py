from collections import OrderedDict
n = int(input())
dic={}
dic=OrderedDict()
for x in range(n):
    item,space,price = input().rpartition(" ")
    #print(f"item : {item}   price : {price}")
    if item in dic:
        dic[item]=dic[item]+int(price)
    else:
        dic[item]=int(price)

for x in dic:
    print(x,dic[x])


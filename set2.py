#a=set(map(int,input().split()))
#b=set(map(int,input().split()))
#a = {2,4,5,9}
#b={2,4,11,12}
i = a.intersection(b)
print(i)

un = a.union(b)
print(un)
ans=list(un.difference(i))
ans.sort()
m=set(ans)
for x in ans:
    print(x)
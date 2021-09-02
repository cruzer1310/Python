from collections import defaultdict

d = defaultdict(list)
l = list(input().split())
m = list(input().split())
for i in range(len(l)):
    d[l[i]].append(i+1)

for i in m:
    if i in d:
        m=d[i]
        
        print(" ".join(map(str,d[i])))
    else:
        print(-1)

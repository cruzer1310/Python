from itertools import permutations
n,p = input().split()
l = list(permutations(n,int(p)))
#l.sort()
for i in l:
        for x in i:
            print(x,end="")
        print()
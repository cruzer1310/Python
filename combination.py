from itertools import combinations

s,x=input().split()

for i in range(int(x)):
    for j in combinations(sorted(s),i+1):
        print("".join(j))
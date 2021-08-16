import itertools
word,num=map(str,input().split())
out = list(itertools.permutations(word,int(num)))
out.sort()
for x in out:
    print("".join(x))


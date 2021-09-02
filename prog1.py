n,m = input().split()
a1 = (input().split())
like = set(input().split())
dislike = set(input().split())
score = 0

for x in a1:
    if x in like:
        score+=1
    if x in dislike:
        score-=1

print(score)
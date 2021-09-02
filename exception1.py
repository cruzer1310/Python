n = int(input())
l=[]
for i in range(n):
    l.append(list(input().split()))

print(l)

for i in range(n):
    
    try:
        print(int(l[i][0])/int(l[i][1]))
    except ZeroDivisionError as e :
        print(e)
    except ValueError as e:
        print(e)

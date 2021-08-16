# Enter your code here. Read input from STDIN. Print output to STDOUT#size = {}
n=int(input())
size=list(map(int,input().split()))
c=int(input())
count=0
for x in range(c):
    cust=list(map(int,input().split()))
    if(cust[0] in size):
        count+=cust[1]
        size.remove(cust[0])
print(count)
from collections import namedtuple

n = int(input())
#a,b,c,d=input().split()
col = input().split()
Student = namedtuple('Student',col)
total = 0
for i in range(n):
    c1,c2,c3,c4=input().split()
    s=Student(c1,c2,c3,c4)
    total+=int(s.MARKS)
    #print(s)


print(f"{(total/n):.2f}")
#x=Student(a=1,b=5,c=6,d=8)
#print(x)
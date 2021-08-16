n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
total = 0.0
for _ in range(n):
    #print(sum(student_marks[name]))
    if(query_name==name):
        total=sum(student_marks[name])
    else:
        continue

print (round((total/3),2))
#print(total)
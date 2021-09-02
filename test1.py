n = int(input())
names=[]
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    names.append(name)
query_name = input()

total = 0.0
for x in range(n):
    #print(sum(student_marks[name]))

    print (names[x])
    """
    print("\n *****************")
    print(query_name)
    print(name)
    if(query_name==name):
        total=sum(student_marks[name])
    else:
        continue

    """

print (format((total/3),'.2f'))
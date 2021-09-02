#Sun 10 May 2015 13:54:36 -0700
#Sun 10 May 2015 13:54:36 -0000
#Sat 02 May 2015 19:54:36 +0530
#Fri 01 May 2015 13:54:36 -0000
from datetime import datetime
t1= input()
t2= input()

time1 = datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
time2 = datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
#a,b,c=str(abs(time1-time2).split(":"))
#total = a*3600+b*60+c
#print(total)
x = abs(time1-time2)

print(x.days*24*3600+x.seconds)
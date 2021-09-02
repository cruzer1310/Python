import calendar

m,d,y=input().split()
#print(f"day : {d}   month : {m}   year: {y}")
day ={0:"MONDAY",1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY",6:"SUNDAY"}
ans = calendar.weekday(int(y),int(m),int(d))
print(day[ans])


# https://docs.python.org/2/library/calendar.html#calendar.TextCalendar
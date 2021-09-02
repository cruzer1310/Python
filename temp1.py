s="#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"
f="qA2"
count=0
last=len(f)
a=b=c=d=e=0
for x in f :
    print(x)
    print(count)
    print("**************")
    if(count==5):
        break
    if(x.isalpha() and b==0):
        print(" alpha")
        b=1
        count=count+1
    elif(x.isalnum() and a==0):
        print("alnum")
        a=1
        count=count+1
    elif(x.isdigit() and c==0):
        print("digit")
        c=1
        count=count+1
    elif(x.islower() and d==0):
        print("lower")
        d=1
        count=count+1
    elif(x.isupper() and e==0):
        print("upper")
        e=1
        count=count+1
    else:
        continue

print(count)
    

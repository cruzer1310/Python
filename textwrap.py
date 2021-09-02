import textwrap
n="hekko"
x=int(input())
s = textwrap.wrap(n,x)
out=""
for i in s:
    out=out+i+"\n"
print (out)
    


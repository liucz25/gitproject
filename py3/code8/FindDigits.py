#!/usr/bin/env python3
file=open('/home/shiyanlou/Code/String.txt')
s=file.read()
print (s)
i=0
out=""
while i<len(s):
    o=s[i:i+1]
    if o.isdigit():
       out+=o
print(out)

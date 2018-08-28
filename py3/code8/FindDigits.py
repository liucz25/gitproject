#!/usr/bin/env python3
file=open('/home/shiyanlou/Code/String.txt')
s=file.read()
i=0
out=""
while i<len(s):
    o=s[i:i+1]
    if o.isdigit():
        out+=o
    i+=1
print(out)

#!/usr/bin/env python3
while True:
    n= int (input("Please enter an Interger:"))
    if n< 0:
        print ("error input")
        continue
    elif n==0:
        break
    print ("Square is ",n**2)
print("Goodbye")

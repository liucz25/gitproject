#!/usr/bin/env p://github.com/liucz25/gitproject.git
import sys

#print ("canshu1",sys.argv[0])
#print ("canshu2",sys.argv[1])
min=int (sys.argv[1])
def mth(min):
        
    h=int(min / 60)
    m=min%60
    print (h," H,",m,"M")
def main ():
    try:
        if min >= 0:
            mth(min)
        else:
            raise ValueError
    except ValueError:
        print("Input number connet be negative")
main()

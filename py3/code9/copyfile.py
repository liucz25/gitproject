#!/usr/bin/env python3
import sys
if len(sys.argv)<3:
    print ("Wrong parameter")
    print ("./copyfile.py OrginFile TargetFile")
    sys.exit(1)
fo=open(sys.argv[1])
s=fo.read()
fo.close()
ft=open(sys.argv[2],'w')
ft.write(s)
ft.close()

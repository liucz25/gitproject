#!/usr/bin/env python3

import sys
import os

def parse_file(path):
    fd=open(path)
    i=0
    spaces=0
    tabs=0

    for i,line in enumerate(fd):
        spaces+=line.count(' ')
        tabs+=line.count('\t')
    fd.close()

    return spaces,tabs,i+1

def main(path):
    if os.path.exists(path):
        spaces,tabs,lines=parse_file(path)
        print("spaces{},tabs{},lines{}".format(spaces,tabs,lines))
        return True
    else:
        return Flase


if __name__=='__main__':
    if len(sys.argv)>1:
        main(sys.argv[1])
    else:
        print("Please input filename of stat after")
        print("1 parameter 0 given")
        sys.exit(-1)
    sys.exit(0)

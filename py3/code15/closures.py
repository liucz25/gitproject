#!/usr/bin/env python3

def line_config(k,b):
    def line(x):
        # line is a closures (bibao)
        return x*x*k +b*x + b
    return line


if __name__=='__main__':
    zhixian=line_config(2,3)
    value=zhixian(5)
    print(value)

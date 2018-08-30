#!/usr/bin/env python3

def my_generator(n):
    print("Inside my genrator")

    yield 'a'
    print("test")
    yield 'b'
    yield 'c'
    for i in range(n):
        yield i
        print("a")
        i += 1
    print("OK")

if __name__=='__main__':
    for char in my_generator(12):
        print(char,end=' ')

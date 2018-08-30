#!/usr/bin/env python3

def my_decorator(func):
    def wrapper(canshu1,cs2):
        print("Before call")
        result = func(canshu1,cs2)
        print("After call")

        return result
    print("decorator ok")

    return wrapper

if __name__=='__main__':
    @my_decorator
    def add(a,b):
        return a + b

    print(add(2,3))

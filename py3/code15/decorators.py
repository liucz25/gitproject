#!/usr/bin/env python3

def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Before call")
        result = func(*args,**kwargs)
        print("After call")
        return result
    return wrapper

if __name__=='__main__':
    @my_decorator
    def add(a,b):
        return a + b

    print(add(2,3))

### Fibonacci example

class Fib:
    def __init__(self, nn):
        self.__n = nn # number of iterations 
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret # this makes p1 and p2 run over ierations
        return ret

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self): # turn an iterable into an interator to be ready for iteration 
        print("Class iter")
        return self.__iter


object = Class(8)

for i in object: # this will invoke the __iter__ method of instance object 
    print(i)


# step by step what python will execute: 
# iterator = object.__iter__()
# Class.__iter__(object) 
# iterator = Fib(8)
# loop starts calling __next__() repeatedly

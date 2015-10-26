# coding : utf-8
import sys
from datetime import datetime

def decor(acync= False, timed= False):
    def ny_dec(func):
        print('111111111')

        def wrap():
            if acync:
                pass
            if timed:
                print(datetime.now())

            print('i am')
            return func()
        return  wrap
    return ny_dec


# raspberry pi
def func():
    print('i am func')

@decor()
def func():
    pass


@decor(acync= True)
def func1():
    pass



@decor(timed= True)
def func2():
    pass



@decor()
def func3 ():
    pass











sys.exit(0)









from datetime import datetime
def dekor_math(func):
    def new_func(*args, **kwargs):
        print('математическое  действие : ', func.__name__, len(args))
        return func(*args, **kwargs)
    return new_func

def dekor_date(func):
    def new_func(*args, **kwargs): #new_func(a,b)
        print(datetime.now())
        return func(*args, **kwargs)
    return new_func


@dekor_date
@dekor_math
def sum_todo(a,b):
    s = a + b
    return s


print(sum_todo(2,3))


@dekor_date
@dekor_math
def sin_a(a):
    pass

print(sin_a(30))

@dekor_date
@dekor_math
def mult_todo(a,b):
    s = a * b
    return s

print(mult_todo(2,3))





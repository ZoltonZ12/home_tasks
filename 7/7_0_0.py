import sys
def dekor(func):
    print('START')
    def new_func():
        print('до')
        func()
        print('после')
    return new_func
    print('END')

sys()

dekor()


@dekor

def some_func():
    for a in  range(10):
        print(a)

some_func()





sys.exit(0)


@now_time
def create_func(param):
    def newFunc():
        for i  in range(10):
            yield a
        return newFunc


o = create_func(1) # на экран еще и время выведеться.


o()
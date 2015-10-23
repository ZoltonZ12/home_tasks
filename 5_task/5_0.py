# coding: utf-8
import sys








sys.exit(0)



a1= {'a':'1','b':'2'}
a2 = {'a':'9','c2':'d'}

for i in a2:
    print(a2[i])


a1.update(a2)
print (a1,a2)




print(__name__)
print (sys.path)# по этим путям ищет питон модули.
#  добавить можно sys.path.append('../')(это ну уровень выше)
e=16

def func():
    from math import e
    print(e)
if __name__ == '__main__':# отсекает  область импорта при импортировании модуля.
    #иначе  внячале импортныется функция, потом будет выполняться весь код в моеле который импортируется.

    func()
    print(e)







sys.exit(0)















name = 3
def test(x):
    global name

    y=x**x
    return y*name


print(test(x=3))
#__all__ позволяет при импорте не только по "*" , но и при простом импорте, импортировать только то что в нем указанно явно.
# __all__ = (cos, sin, tg)
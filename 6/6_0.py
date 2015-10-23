# coding: utf-8
#генераторы выражение генератор  в () внутри обычный [] НО С ОТЛОЖЕНЫМ ВЫПОЛНЕНИЕМ.
# ВЫЧЕСЛЯЮТСЯ ПО ЭЛЕМЕНТНО.
import sys





sys.exit()

def gen2(n):
    yield 30
    yield 20
    yield 10


s= gen2(3)
print(next(s))
print(next(s))
print(next(s))

sys.exit()






gen = (x**2 for x in range(10)) # выражение-генератор


for i in gen:
    print(i)

# универсальный генератор yield/ елис есть в функции  yeild то функция воспринимается как генератор
# ГНератор НЕ ИТЕРИРУЕМЫЙ обьект. [0] не работает.




def gen1(n):
    yield 30
    for i in range(n):
        yield i**2
    for i in range(n, 0, -1):
        yield i**2
for i in gen1(4):
    print(i)
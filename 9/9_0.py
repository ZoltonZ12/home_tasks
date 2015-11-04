# наследование классов.!!!!!!!
# берется класс словарь и изменяется только один метод ГЕТ .

import sys

class Boiler():
    volume = 0


class Car():
    k = 1
    def __init__(self,model =0):
        self.model = model
    def run(self):
        time_dis = float(input('введите время в пути ...'))
        #print(self.k)
        distance = time_dis * self.k
        return distance

class F1(Car):
    k = 7

class Truck(Car):
    k = 15



truk = Truck()

car = Car()

f1 = F1()


print(car.run(), truk.run(),  f1.run() )



sys.exit(0)




print ([a for  a in dir(Truck('Volvo')) if not  a.__name__.startswith('_') ])


print(dir(Car()) == dir(F1()) == dir(Truck()) )



class Mydack(dict):
    def get(self, key, default = 0):
        return dict.get(self, key , default)


class Mydack1(Mydack):
    pass




a = dict(a=1,b=2)
b = Mydack(a=1,b=2)

b['c'] = 4
print(b)

b['v']
print(b)

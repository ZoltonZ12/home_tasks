# coding: utf-8

import sys, random
from abc import ABCMeta,abstractmethod


class ABC_Animal(metaclass=ABCMeta):
    @abstractmethod
    def month_has_pass(self):
        pass


#r1 = random.randrange(0,100,1) внезабная болезнь.
# print(r)




class Animal(ABC_Animal):# как правильно создавать в ините свойства животного или кака аргументы ?
    def __init__(self):
        self.age_mounth = 0
        self.distanse = 0
        self.voice = str(None)
        self.sex = bool(random.randrange(0,2)) # False == Famele, True == Male. как задать два варианта из  не стандартных  ТРУ /фалсе
        self.product = str(None)
        self.product_per_mounth = int(0)
        self.product_total = int(0)
        self.health = 100
        self.life_age_year = 100

    def run(self, x):
        self.distanse += x




    def month_has_pass(self):
        self.age_mounth += 1
        self.product_total += self.product_per_mounth
        if self.life_age_year*12 - self.age_mounth <0:
            self.health = random.randrange(0,2)
            if self.health == 0:
                print('animal has die')
                del self # проверить правильно ли это убивает обьект.
            else:
                pass
        elif self.life_age_year/3.*2.< (self.age_mounth/12) < self.life_age_year:
            rand_range_ill = self.life_age_year*12 - self.age_mounth # 60 90  90-61=29   90-89=1
            self.health = random.randrange(0,rand_range_ill)# всякие болезни, старость и тд. сокращающие жизнь анимала

            if self.health == 0:
                print('animal has die')
                del self # проверить правильно ли это убивает обьект.
            else:
                pass



class Duck(Animal):
    product = 'eggs'
    def __init__(self):
        super().__init__()
        self.voice = 'krya-krya'
        self.life_age_year = 5

        self.product_per_mounth = int(random.randrange(20,30))

    def __repr__(self):
        return 'утка'

    def __str__(self):
        return 'утка'


class Cow(Animal):
    product = 'milk'
    def __init__(self):
        super().__init__()
        self.voice = 'Muuuu'
        self.life_age_year = 10

        self.product_per_mounth = int(random.randrange(7*30,16*30))

    def __repr__(self):
        return 'корова'

    def __str__(self):
        return 'корова'

class Dog(Animal):
    #super().voice = 'Gav-gav-gav-gav-gav' так не работает . почему ???
    # voice = 'Gav-gav-gav-gav-gav' так тоже.
    product = 'garde' # вынес в свойства так как,впоследствии удобно использовать при отчетах атрибуты не создавая обьект .!!!
    def __init__(self):
        super().__init__()
        self.voice = 'Gav-gav-gav-gav-gav'
        self.life_age_year = 15

        self.product_per_mounth = int(random.randrange(1,101))
    def __repr__(self):
        return 'собака'

    def __str__(self):
        return 'собака'


class Farm(ABC_Animal):

    def __init__(self, dogs = 0, ducks = 2, cows = 2):
        self.age_farm = 0
        self.list_dogs = []
        self.product_dogs = 0
        self.list_ducks = []
        self.product_ducks = 0
        self.list_cows = []
        self.product_cows = 0
        for i in range(dogs):
            self.list_dogs.append(Dog())
        for i in range(ducks):
            self.list_ducks.append(Duck())
        for i in range(cows):
            self.list_cows.append(Cow())

    def month_has_pass(self):
        self.age_farm += 1
        self.product_dogs = 0
        self.product_ducks =0
        self.product_cows = 0
        for i  in self.list_dogs:
            i.month_has_pass()


            self.product_dogs +=  i.product_total
        for i  in self.list_ducks:
            i.month_has_pass()

            self.product_ducks +=  i.product_total
        for i  in self.list_cows:
            i.month_has_pass()
            self.product_cows +=  i.product_total
        pass

    def table_all(self):
        print('прошло {}  месяцев существования фермы. '.format(self.age_farm))
        print('На ней живет: \n Уток \t {} \n коров \t {} \n собак \t {}'.format(len(self.list_ducks),len(self.list_cows),len(self.list_dogs)))
        for  cont,i  in enumerate(self.list_ducks):
            print('Утка номер {} произвела {} {}'.format(1+cont, i.product_total, i.product)) # перестало работать когда перенес из инита в атрибуты . почему ?

        for  cont,i  in enumerate(self.list_cows):

            print('Корова номер {} произвела {} {}'.format(1+cont, i.product_total, i.product))
        for  cont,i  in enumerate(self.list_dogs):

            print('Собака номер {} произвела {} {}'.format(1+cont, i.product_total, i.product))
        print('Всего произведено: \n {} \t {}  \n {} \t {} \n {} \t {} '.format(self.product_ducks, Duck.product ,self.product_cows, Cow.product,self.product_dogs, Dog.product))
farm1 = Farm(dogs=1,cows=4)

cow1321312 = Cow()
print(cow1321312)


sys.exit(0)

farm1.month_has_pass()
farm1.month_has_pass()
farm1.month_has_pass()

farm1.table_all()




for i, month in enumerate(range(100)):
    farm1.month_has_pass()
    print('идет  ',(1+month), ' месяц', ' количество уток - ', farm1.list_ducks,farm1.age_farm)
print(farm1.list_ducks[0].product_total)
print(farm1.list_ducks[0].month_has_pass())


# coding: utf-8

import sys, random



#r1 = random.randrange(0,100,1) внезабная болезнь.
# print(r)




class Animal:# как правильно создавать в ините свойства животного или кака аргументы ?
    def __init__(self):
        self.age_mounth = 0
        self.distanse = 0
        self.voice = str(None)
        self.sex = bool(random.randrange(0,2)) # False == Famele, True == Male. как задать два варианта из  не стандартных  ТРУ /фалсе
        self.product = str(None)
        self.product_per_mounth = int(0)
        self.health = 100
        self.life_age_year = 100

    def run(self, x):
        self.distanse += x




    def month_has_pass(self):
        self.age_mounth += 1
        if self.life_age_year*12 - self.age_mounth <0:
            print('animal has die')
            del self # проверить правильно ли это убивает обьект.




class Duck(Animal):
    def __init__(self):
        super().__init__()
        self.voice = 'krya-krya'
        self.life_age_year = 5
        self.product = 'eggs'
        self.product_per_mounth = int(random.randrange(20*30,30*30))



class Cow(Animal):
    def __init__(self):
        super().__init__()
        self.voice = 'Muuuu'
        self.life_age_year = 10
        self.product = 'milk'
        self.product_per_mounth = int(random.randrange(7*30,16*30))

class Dog(Animal):
    #super().voice = 'Gav-gav-gav-gav-gav' так не работает . почему ???
    # voice = 'Gav-gav-gav-gav-gav' так тоже.
    def __init__(self):
        super().__init__()
        self.voice = 'Gav-gav-gav-gav-gav'
        self.life_age_year = 15
        self.product = 'garde'
        self.product_per_mounth = int(random.randrange(1,101))



class Farm():

    def __init__(self, dogs = 0, ducks = 2, cows = 2):
        self.list_dogs = []
        self.list_ducks = []
        self.list_cows = []
        for i in range(dogs):
            self.list_dogs.append(Dog())
        for i in range(dogs):
            self.list_ducks.append(Duck())
        for i in range(dogs):
            self.list_cows.append(Cow())

    def month_has_pass(self):
        pass



farm1 = Farm(dogs=1, cows=4)

print(farm1.list_ducks[0].product)



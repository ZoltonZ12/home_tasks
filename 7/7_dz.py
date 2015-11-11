class TANK:

    speed = 0 # любой танк создается стоячим.

    def __init__(self):
        print('создается танк')
        self.model = input('введите модель танка')
        self.shassi = input('введите количество шасси')
        self.gus = input('введите наличие гусенец а')


    def status(self, sp = speed ):
        if self.speed > 0:
            return True
        else:
            return False


class CAR:

    speed = 0

    def __init__(self):
        print('создается машина')
        self.model = input('введите модель машины')
        self.wells = input('введите количество колес')


    def status(self, sp = speed ):
        if self.speed > 0 and self.wells ==4 :
            return True
        else:
            return False

class TELEGA:

    speed = 0

    def __init__(self):
        print('создается телега')
        self.wells = input('введите количество колес')

    def status(self, sp = speed ):
        if self.speed > 0 and self.wells == 4 :
            return True
        else:
            return False



car_1 = CAR()
car_1.speed = 20

tank_1 = TANK()
tank_1.speed = 2

telega_1 = TELEGA()
telega_1.speed = 0

car = [tank_1,car_1, telega_1]
for i in  car:
    print(i, i.status()) # выводит не имя  обьекта!!!
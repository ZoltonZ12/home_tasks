class A:
    x= 100# эта переменная видна извне как атрибут класса . например  A.x
    _z= 100# эта переменная видна извне как атрибут класса . например  A._z
    __y = 10 # этот атрибут  извне не видет. интерпритатор его прячет в таком виле. _A__y




# абстрактные классы .  пример подключение новый систем оплаты,  при этом в каждой нужно  описать абстрактный
# метод , подтврждение платежа.




class Woker_1:
    price_1_month  = 10000
    def make_remont(self):
        print('Work by woker_1')
        return self.price_1_month


class Woker_2:
    price_1_month  = 15000
    def make_remont(self):
        print('Work by woker_2')
        return self.price_1_month

class Prorab:
    price_1_month  = 30000
    def __init__(self):
        self.wokers = Woker_1() # здесь где то делегтрование.
        pass
    def make_remont(self):
        print('Work by prorab + etc')
        wp = self.price_1_month
        return self.price_1_month + wp

p = Prorab()
price = p.make_remont()

print('remont: ', price)
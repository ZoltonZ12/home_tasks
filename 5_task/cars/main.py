# coding: utf-8

from db import main_menu
from debug import filt_by_pow, filt_by_name


#if __name__ is '__main__':

while 1:
    data = main_menu()
    filt = input('выберите тип фильтрации 1- без фильтра, 2-по мощьности, 3- по названию ')

    try:
        if filt == '1':
            for i in data.items():
                print ('марка машины -{},  мощьность ее - {} '.format(*i))
        elif filt == '2':
            data = filt_by_pow(data)
            for i in data.items():
                print ('марка машины -{},  мощьность ее - {} '.format(*i))
        elif filt == '3':
            data = filt_by_name(data)
            for i in data.items():
                print ('марка машины -{},  мощьность ее - {} '.format(*i))
        else:
            print('необходимо выбрать  цыфры действия')
            continue

    except: # так как не передаю сюда знаечния data, тем самым  разделяю input и output.
        pass



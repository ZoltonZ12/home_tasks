# coding: utf-8

from db import main_menu
from debug import filt_by_pow


if __name__ is '__main__':

    while 1:
        data = main_menu()
        try:
            data = filt_by_pow(data)
            #print(data)
            for i in data.items():
                print ('марка машины -{},  мощьность ее - {} '.format(*i))
        except: # так как не передаю сюда знаечния data, тем самым  разделяю input и output.
            pass



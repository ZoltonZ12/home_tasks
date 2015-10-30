# coding : utf-8

import os, sys, time,pickle


a = { 'modul_1': False, 'modul_2': False, 'modul_3': False, }


def bd_wr(a):
    f = open('db.pickle', 'wb')
    pickle.dump(a, f , 2)
    f.close()

def bd_read():
    f = open('db.pickle', 'rb')
    a = pickle.load(f)
    f.close()
    return a

bd_wr(a)
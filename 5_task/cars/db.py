# coding: utf-8

import os, pickle


db_file = 'bd.pickle'


def bd_pikle_read():
    if db_file in os.listdir():
        f = open(db_file, 'rb')
        data = pickle.load(f)
        f.close()
    else:
        data = {}
    return data


def bd_pikle_write(data):
    f = open(db_file, 'wb')
    pickle.dump(data, f)
    f.close()


def input_func():
    single_data={}
    print('введите марку автомобиля и мощьность')
    while 1:
        mark = input('Марка : \n')
        if mark.isalpha():
            break
        else:
            print('марка должна содержать только буквеные символы')

    while 1:
        power = input('Мощьность :\n')
        if power.isdigit():
            break
        else:
            print('мощьность должна содержать только цыфры')
    single_data[mark] = power
    data = bd_pikle_read()
    data.update(single_data)
    bd_pikle_write(data)
    #return data


def  main_menu():
    todo = input('чего изволите ? 1-ВВЕСТИ или 2- ВЫВЕСТИ ? а возможно  3-УДАЛИТЬСЯ ?...\n')
    FUNCS = {
    '1': input_func,
    '2': output_func,
    '3': exit_func
        }
    if todo in FUNCS:
        return FUNCS[todo]()

    else:
        print('Нужно ввыести цыфры соответствующие командам...')
        main_menu()


def output_func():
    data = bd_pikle_read()
    try:
        if len(data) == 0:
            print('база пока ещё пуста, её надо наполнить')
            return {}
        else:
            return data
    except:
        pass


def exit_func():
    exit()

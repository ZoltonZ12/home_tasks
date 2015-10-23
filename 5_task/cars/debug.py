# coding: utf-8


def more_then(data):
    val=input('введите значение мощьности \n')
    if val.isdigit():
            for j  in [i for i in  data.items() if i[1] > val]:
                    return (j)
    else:
        print('не верной указаны параметры фильтра(скорее всего не цыфры)')
        more_then(data)




def filt_by_pow(data):
    type_sub_sort = input('хотите найти  мощьность .\n 1 - равную \n 2 - больше, чем ..  \n 3 - меньше, чем ..  \n 4 - больше чем Х и меньше чем У..  \n' )
    while 1:
        if type_sub_sort == '1':
            val=input('введите значение мощьности \n')
            if val.isdigit():
                new_data = {i[0]:i[1] for i in  data.items() if i[1] == val}
                return new_data
                break
            else:
                print('не верной указаны параметры фильтра(скорее всего не цыфры)')
                continue
        elif type_sub_sort == '2':
            val=input('введите значение мощьности \n')
            if val.isdigit():
                new_data = {i[0]:i[1] for i in  data.items() if i[1] > val}
                return new_data
                break
            else:
                print('не верной указаны параметры фильтра(скорее всего не цыфры)')
                continue

        elif type_sub_sort == '3':
            val=input('введите значение мощьности \n')
            if val.isdigit():
                new_data = {i[0]:i[1] for i in  data.items() if i[1] < val}
                return new_data
                break
            else:
                print('не верной указаны параметры фильтра(скорее всего не цыфры)')
                continue

        elif type_sub_sort == '4':
            val=input('введите значение мощьности в виде Х,У \n')
            if val.split(',')[0].isdigit() and val.split(',')[1].isdigit():
                new_data = {i[0]:i[1] for i in  data.items() if i[1] < val.split(',')[1] and i[1] > val.split(',')[0]}
                return new_data
                break
            else:
                print('не верной указаны параметры фильтра(скорее всего не цыфры)')
                continue

        else:
            continue


def filt_by_str():
    pass

def filt_by_name():
    pass

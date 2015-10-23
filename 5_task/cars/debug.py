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


def filt_by_name(data):

    type__sub_sort = input('хотите найти  по:\n 1 - вхождению  части слова  в имя модели  \n 2 - точному совпадению  модели \n ' )
    if type__sub_sort == '1':
        while 1:
            val=input('введите часть слова \n')
            if val.isalpha():

                new_data = {i[0]:i[1] for i in  data.items() if val in  i[0]}
                print(new_data)
                return new_data
                break
            else:
                print('не верной указаны параметры фильтра(скорее всего не буквы)')
                continue

    elif type__sub_sort == '2':
        val=input('введите искомую модель \n')
        while 1:
            if val.isalpha():
                if val.isalpha():
                    new_data = {i[0]:i[1] for i in  data.items() if val in  i[0]}
                    return new_data
                    break
            else:
                print('не верной указаны параметры фильтра(скорее всего не буквы)')
                continue
    else:
        print(' Необходимо выбрать цыфры соответствующих фильтров')
        filt_by_name(data)



# coding utf-8

import pickle
data = []

#f = open('bd.pickle','wb') создание базы  раскоментировать в первый запуск.
#pickle.dump(data,f,2)
#f.close()
while 1:
    todo = input('чего изволите ? 1-ВВЕСТИ или 2- ВЫВЕСТИ ? а возможно  3-УДАЛИТЬСЯ ?...\n')
    if todo.lower() == 'ввести' or todo.lower() == '1':
        data_file = open('bd.pickle','rb')
        data = pickle.load(data_file)
        data_file.close()
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
        data.append((mark,power))
        f = open('bd.pickle','wb')
        pickle.dump(data,f,2)
        f.close()
        
    elif todo.lower() == 'вывести' or todo.lower() == '2':
        data_file = open('bd.pickle','rb')
        data = pickle.load(data_file)
        data_file.close()
        if len(data) == 0:
                        print('база пока ещё пуста, её надо наполнить')
                        continue
        while 1:
            sub_do= input('Хотите использовать фильтр ? 1-да , 2-нет ')
            if sub_do.lower() == 'да' or sub_do.lower() == '1':
                type_sort = input('выберите тип сортировки.\n 1 - сортировка по мощности \n 2 - сортировка по названию \n')
                if type_sort == '1':
                    type__sub_sort = input('хотите найти  мощьность .\n 1 - равную \n 2 - больше, чем ..  \n 3 - меньше, чем ..  \n 4 - больше чем Х и меньше чем У..  \n' )
                    if type__sub_sort == '1':
                        
                        val=input('введите значение мощьности \n')
                        if val.isdigit():
                            for j  in [i for i in  data if i[1] == val]:
                                print(j)
                            break
                        else:
                            print('не верной указаны параметры фильтра(скорее всего не цыфры)')
                            continue
                    elif type__sub_sort == '2':
                        val=input('введите значение мощьности \n')
                        if val.isdigit():
                            for j  in [i for i in  data if i[1] > val]:
                                print(j)
                            break
                        else:
                            print('не верной указаны параметры фильтра(скорее всего не цыфры)')
                            continue
                        
                    elif type__sub_sort == '3':
                        val=input('введите значение мощьности \n')
                        if val.isdigit():
                            for j  in [i for i in  data if i[1] < val]:
                                print(j)
                            break
                        else:
                            print('не верной указаны параметры фильтра(скорее всего не цыфры)')
                            continue
                        
                    elif type__sub_sort == '4':
                        val=input('введите значение мощьности в виде Х,У \n')
                        if val.split(',')[0].isdigit() and val.split(',')[1].isdigit():
                            for j  in [i for i in  data if i[1] < val.split(',')[1] and i[1] > val.split(',')[0]]:
                                print(j)
                            break
                        else:
                            print('не верной указаны параметры фильтра(скорее всего не цыфры)')
                            continue
                        pass
                    else:
                        continue
                elif type_sort == '2':
                    type__sub_sort = input('хотите найти  по:\n 1 - вхождению  части слова  в имя модели  \n 2 - точному совпадению  модели \n ' )
                    if type__sub_sort == '1':

                        val=input('введите часть слова \n')

                        if val.isalpha():

                            for j  in [i for i in  data if val in i[0] ]:
                                print(j)
                            break
                        else:
                            print('не верной указаны параметры фильтра(скорее всего не буквы)')
                            continue
                    elif type__sub_sort == '2':
                        val=input('введите искомую модель \n')
                        if val.isalpha():
                            print('/////')
                            for j in [i for i in  data if val == i[0]]:
                                print( len(j))
                                if len([i for i in  data if val == i[0]])==0:# не успеваю доделать.  не выходит сюда. не понятно почему.  тестить дальше не могу.
                                    print('результатов удовлетворяющих поиску - не найдено')
                                else:
                                    print(j )
                                break
                        else:
                            print('не верной указаны параметры фильтра(скорее всего не буквы)')
                            continue
                    else:

                        pass

                else:
                    print('неверно выбраны параметры фильтрации... \n')
                    continue
            elif sub_do.lower() == 'нет' or sub_do.lower() == '2':
                data.sort()
                print('выводиться без фильтров')
                for i  in data:
                    print(i)
                break
            else:    
                data.sort()
                print('выводиться без фильтров')
                for i  in data:
                    print(i)
                break
    elif todo.lower() == 'удалиться' or todo.lower() == '3':
        print('no  exit!!!!!')
        break
    else:
        print('нужно  набрать: ввести ,вывести или выйти \n')
        
        

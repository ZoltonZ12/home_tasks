#coding utf8
while 1:
    a= input('введите число: ')
    try:
        a = float(a) #check  A is number
        break
    except:
        print('должно  быть введено число')
        continue



while 1:

    while 1:
        print('доступные действия :', '\n', '+  сложить', '\n', '- вычестье', '\n', '* умноженить', '\n', '/ разделенить')
        action = input('введите дествие   ')
        if action in ['+','-','*','/']:
            break
        else:
            print('выберете действие из  списка ')
            continue
    while 1:
        b= input('введите следующее число: ')
        try:
            b = float(b)#check  B is number
            break
        except:
            print('должно  быть введено число')
            continue

     
    if action == '+' :
        a = a + b
    elif action == '-' :
        a = a - b
    elif action == '*' :
        a = a * b
    elif action == '/' :
        a = a / b
    else:
        a = 'Error' 
    print('результат =  ', a)
    cont = input('Продолжить ?  y or n   ')
    if cont is 'y':
        print ('Последний результат  = ', a, 'нужно ...')
        pass
    else:
        break

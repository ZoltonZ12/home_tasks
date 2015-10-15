from collections import defaultdict
print('__________2/1__________')
print('создан список')
lst = ['иван иванов','иван петров','вован сидоров','сергей жуков','василий жуков','ринь янь']

print('__________2/2__________')
ind = input('введите индекс студента:  ')
if ind.isdigit():
    print(lst[(int(ind))])
        
else:
    print('должно быть целое число')

print('__________2/3__________')

srez = input('введите срез  студентов от  и до "от, до"')# проверку уже не делаю, так как не в этом суть задания.
srez_list = srez.split(',')

print(lst[(int(srez_list[0])):(int(srez_list[1]))])


print('__________2/4__________')
count_r = 0
liter = 'р'
for i in lst:
    if liter in i.split()[0]:
        count_r +=  1
    else:
        pass
print('колличество студентов у которых  в  имени  содержится буква ', liter , ' = ',count_r)



print('__________2/5__________')

res_list = []

lst.sort()
#print(lst)
temp_list = []
for i in lst:


    #print(i.split()[0])
    if len(temp_list) == 0:
        temp_list.append(i)
        #print(temp_list,'111111111')
        #print(temp_list[0].split()[0])
    elif i.split()[0] ==  temp_list[0].split()[0]: # если поставить вместо ==  is , то всё ломается . встречается подобное  часто.  почему ???
        temp_list.append(i)
        #print(temp_list,'2222222222')
    else:
        res_list.append(temp_list)
        temp_list = []
        temp_list.append(i)
        #print(temp_list,'33333333')
print(res_list,'!!!!!!!!!')
#test auto push git

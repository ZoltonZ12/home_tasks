# coding: utf-8

import sys
from datetime import  datetime,timedelta


print (datetime.now().date())
print(datetime.now().date()- timedelta(days=2))


lst = {'иван иванов':4,'иван петров':5,'вован сидоров':3,'сергей жуков':2,'василий жуков':1,'ринь янь':4}
dict_todo = {'иван иванов':('code 1','2015-10-21'),'иван петров':('code 6','2015-10-20'),
        'вован сидоров':('code 2','2015-10-22'),'сергей жуков':('code 1','2015-10-20'),
        'василий жуков':('code 4','2015-10-19'),'ринь янь':('code 1','2015-10-21')}

now = datetime.now().date()
todo = 'code 1'

def gen3(date, todo):

    for i in dict_todo.items():
        if i[1][0] == todo and i[1][1] == str((datetime.now().date()- timedelta(days=2))):
            yield {i[0]:i[1]}

res = gen3(now,todo)
for i in  res:
    print(i)
    
print(res, '!!!!!!!!!!!!!!!!!!!!')





sys.exit()



gen1 = (x for x in lst.items() if x[1]>=4)


print(gen1)
for i in gen1:
    print(i)


def gen2():
    for i in lst.items():
        if i[1] >= 4:
            yield i
print('______________________________')
print(gen2)

for i  in gen2():
    print(i)













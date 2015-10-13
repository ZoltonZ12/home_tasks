
lst = ['иван иванов','иван петров','вован сидоров','сергей жуков','василий жуков','ринь янь']
ind = input('введите индекс студента:  ')

if ind.isdigit():
    print(lst[(int(ind))])
        
else:
    print('должно быть целое число')

srez = input('введите срез  студентов от  и до "от, до"')
srez_list = srez.split(',')

print(lst[(int(srez_list[0])):(int(srez_list[1]))])

count_r = 0
for i in lst:
    if 'р' in i.split()[0]:
        count_r +=  1
    else:
        pass
print(count_r)


    

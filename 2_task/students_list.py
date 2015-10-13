
lst = ['иванов','петров','сидоров','вавава','ываываыв','аываыва']
ind = input('введите индекс студента:  ')

if ind.isdigit():
    print(lst[(int(ind)-1)])
        
else:
    print('должно быть целое число')

srez = input('введите срез  студентов от  и до "от, до"')
srez_list = srez.split(',')
print(srez_list)
print(lst[(int(srez_list[0])):(int(srez_list[1]))])
        
    

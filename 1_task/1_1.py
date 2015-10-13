#coding utf8
import math
d1 = 45
d2 = 338
d3 = 19
list_circ = [d1,d2,d3]
list_sq = []
for  i in  list_circ:
    sq = round(math.pi*(i/2.)**2,2)
    list_sq.append(sq)
print('площади кругов',list_sq)
list_sq.sort(reverse = True)
res = list_sq[0]
for i in list_sq[1:]:
    res = res - i

print('площадь: из большего вычтено два меньших = ',res)

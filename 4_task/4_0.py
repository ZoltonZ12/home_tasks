import pickle
import os

FILE_NAME = 'LST_SAVED.pickle'
if os.path.exists(FILE_NAME):
    f = open(FILE_NAME, 'rb')
    LST = pickle.load(f)
else:
    LST = [1, 2, 3]

LST.append(len(LST)+1)
f = open(FILE_NAME, 'wb')
pickle.dump(LST, f)
f.close()

print(LST)








s = 'a = b, c = d'

d = {}
for a in s.split(','):
    key,value = [i.strip() for i in a.split('=')]
    d[key] = value


print(d)








a=' 252'
b = 'sss'
b = b + 'aaa'
print
print(a.isdigit())
print(a is b)
print(a,b)




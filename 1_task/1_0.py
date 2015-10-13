import os
path_dir = r'.\1'
print(path_dir)
list_file_name = (os.listdir(path_dir))
python_sum = 0

f_result=open('result.txt','w')#если есть старый файл result, то очишаем его
f_result.close()
for i  in list_file_name:
    f = open(path_dir+'\\'+ i)
    count1 = f.read().count('python')
    if count1:
        print(i, 'содержит ', count1, 'питонов')
        f_result=open('result.txt','a')
        f_result.write(str(i+ ' содержит '+ str(count1)+ ' питонов'+ '\r'))
        f_result.close()
    python_sum = python_sum + count1
    f.close()
text_result = 'итого: '+ str(python_sum) + ' питонов'
print(text_result)
f_result=open('result.txt','a')
f_result.write(text_result)
f_result.close()


# coding: utf-8


import os, sys




def find_file(exc = '.py'):
    for file in os.listdir('.'):
        if file.endswith(exc):
            print(file)
            for st_num, line in enumerate(open(file, encoding='utf-8')):
                yield ( file, st_num, line )

lst = find_file()


sub_str = 'def'

def grep(gen, sub_str):
    for str in find_file():
        if sub_str in str[2]:
            yield ( str )

lst1= grep(find_file, sub_str)



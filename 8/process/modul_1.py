# coding : utf-8

import os, sys, time, common

print(os.path.basename(__file__).split('.')[0])
file_key = os.path.basename(__file__).split('.')[0]

while 1:
    a = common.bd_read()
    a[file_key] = True
    print('!!!!!!!!  start ', a)
    common.bd_wr(a)
    print('1111')
    time.sleep(10)





sys.exit(0)
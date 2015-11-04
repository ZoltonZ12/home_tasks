# coding : utf-8

import os, sys, time, common
import argparse




def stop(func):
    def new_func():
        a = common.bd_read()
        a[file_key] = False
        print('!!!!!!!!   ', a)
        common.bd_wr(a)
        print('1111 stop')


def create_pars():
    parser = argparse.ArgumentParser()
    parser.add_argument('--control', '-c',  nargs = '*' )

    return parser


if __name__ == '__main__':
    parser = create_pars()
    namespace = parser.parse_args()
    if namespace.control != None and  namespace.control[0]== 'stop':
        print('!!!!!!!!')
    print(namespace.control)


'''
Created on 2014年8月21日
@author: lenovo
'''
import binascii
import struct


def example(express, result=None):
    if result == None:
        result = eval(express)
    print(express, ' ==> ', result)


if __name__ == '__main__':
    print('整数之间的进制转换:')
    print("10进制转16进制", end=': ');
    example("hex(16)")
    print("16进制转10进制", end=': ');
    example("int('0x10', 16)")
    print("类似的还有oct()， bin()")

    print('\n-------------------\n')


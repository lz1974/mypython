
import os

myread=open('C:\Users\lz\AppData\LocalLow\HaiBo\书香联萌\log.txt','r')
for line in myread:
    print(line,end='')
myread.close()
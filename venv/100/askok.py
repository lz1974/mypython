# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
http://www.runoob.com/manual/pythontutorial3/docs/html/controlflow.html#tut-functions\
函数定义练习
'''
def ask_ok(por,retries=4,complait='yes or no ,please'):
    while True:
              ok=input(por)
              if ok in('y','ye','yes'):
                  return True
              if ok in('n','no','nop','nope'):
                  return False
              retries=retries-1
              if retries<0:
                  raise OSError("U")
              print(complait)


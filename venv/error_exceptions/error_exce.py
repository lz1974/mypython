# num=6
# print("hello world"+str(num))

while True:
    try:
        x=int(input("please"))
        print(x)
        break
    except ValueError:
        print("error")

#   如果没有出现异常，except将被忽略，直接跳到except语句
#   如果try语句之间出现异常，try 之下异常之后的代码将被忽略，直接跳到except语句
#   如果异常出现，但是不属于except中定义的异常类型，程序将执行外围一层的try语句，如果异常没有呗处理，将产生unbandled exception错误

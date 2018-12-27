

# f=open('test.txt')
# while True:
#     line=f.readline()
#     if len(line)==0:
#         break
#     print(line)
# f.close()


try:
    f=open('test.txt')
    s=f.readline()
    i=int(s.strip()) #
except OSError as err:
    print("OS errer:{0}".format(err))
except ValueError:
    print("no integer")
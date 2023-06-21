''' isinstance 是否是某个类型的实例, 类似于 instance of '''
n = 1
# 是否是 int 类型， 是的。为 True
print(isinstance(n,int))
# 是否为 float 类型，不是的，为 False
print(isinstance(n,float))
# 是否为 float,int,str 里的一个。 是的，为 True
print(isinstance(n,(float,int,str)))

'''type() 表示类型'''
print(type(3))
print(type(4.5))
print(type('abcd'))

n = 23
# type 比较
if type(n)==int:
    print("%s是int类型"%n)
else:
    print("%s不是int类型"%n)
# isinstance 比较
if (isinstance(n,int)):
    print("%s是int类型"%n)
else:
    print("%s不是int类型"%n)
# 查询最大数
import sys
print(sys.maxsize) # 9223372036854775807

# boolean 类型值 True False
n = 3
print(bool(n))



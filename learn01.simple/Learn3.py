# str() 函数
a =3
print(str(3))
# 定义 Person 对象处理
class Person:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def __str__(self):
        return "%s今年%s岁"%(self.name, self.age)
person = Person('张三',25)
print(str(person))

# chr() 转换成 单个字符
print(chr(0x31))
print(chr(90))

# hex 转换为 十六进制  bin() 二进制  oct() 八进制
print(hex(65))
print(bin(4))
print(oct(9))

# 小游戏，打印信息值
# start = int(input("请输入开始值:"))
# end = int(input("请输入结束值:"))
# print("十进制 八进制 十六进制 字符")
# for i in range (start,end+1):
#     print("{} \t {} \t {}\t{} \t".format(i,oct(i),hex(i),chr(i)))

# ord(x) 转换成十进制整数
print(ord('a'))
print(ord('A'))

# float() 转换为浮点数
pi = 3.14
r = float(input("请输入圆的半径:"))
h = float(input("请输入圆柱的高:"))
c =2*pi*r
sa = pi*r**2;
sb = 4*pi*r**2;
va =4/3*pi*r**3
vb =sa*h
print("圆的周长 2pR:",c)
print("圆的面积: piR的平方",sa)
print("球的表面积: 4piR的平方",sb)
print("球的体积:4/3 pi R的三次方",va)
print("圆柱的体积: 圆的底面积*h",vb)
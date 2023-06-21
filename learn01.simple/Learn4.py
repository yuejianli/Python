'''
条件表达式:   True表达式 if 条件表达式 else false 表达式
'''
#
# n = int(input("请输入一个数字:"))
# x=n if n>=0 else -n
# print("打印输入数字 %s的绝对值:%s"%(n,x))

# username = input("请输入用户名:")
# password =input("请输入密码：")
# result = "登录成功" if (username=='admin' and password=="123") else "用户名或者密码错误"
# print(result)

print(5/3)
print(5//3)

# 计算一个数的阶乘
import math
print(math.factorial(3))

# 或者自定义阶乘算法
def factorial(n):
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))



# 计算 1到 100 以内的所有的偶数和
# sum = 0
# for i in range (100):
#     if (i %2 == 0):
#         sum += i
# print("1到100的总和是:%s"%(sum))

num = 0
strnum = 0
content =input("请输入要统计的内容:")
for i in content:
    if i.isdecimal():
        num +=1
    elif i.isalpha():
        strnum +=1
    else:
        pass
print("数字的个数是:",num)
print("字符的个数是:",strnum)

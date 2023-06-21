# 不写循环了  阿姆斯特朗数
# n = int(input("输入的数字:"))
# len = len(str(n))
# s = 0
# t = n
# while t>0:
#     d = t %10
#     s += d ** len
#     t= t //10
# if s == n :
#     print("%d 是阿姆斯特朗数" %n)
# else:
#     print("%d 不是阿姆斯特朗数" %n)

# 密码验证
'''
用户密码验证程序，要求密码输入只有3次机会，
且密码中不能包含"*"字符。本例需要考虑3个问题：验证次数、特殊限制和正误密码判断。
验证次数使用无限循环实现，要注意3个分支的先后顺序：正确密码、特殊字符检测和错误密码
'''

# count = 3
# password = '123456'
# canLogin = False
# while count > 0:
#     inputPs = input("请输入密码:")
#     if ( password == inputPs):
#         canLogin = True
#         break
#     elif ("*" in inputPs):
#         print("密码里面不能有特殊字符 * ")
#         count-=1
#         continue
#     else:
#         print("密码输入错误")
#         count-=1
#         continue
# if (canLogin):
#     print("密码输入正确,登录成功")
# else:
#     print("密码输入3次错误，被锁定")
#

# 九九乘法表
for i in range (1,10):
    for j in range (1,i+1):
        print("%d*%d=%d" %(i,j,i*j),end=" ")
    print()
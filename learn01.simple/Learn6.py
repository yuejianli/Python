# 数字添加功能
# list = [1,2,3,4,5,6]
# while True:
#     num = int(input("请输入一个数字:"))
#     if num in list:
#         print("数字 %s 已存在列表中"%num)
#     else:
#         print("数字 %s 不存在列表中,进行添加到列表中"%num)
#         list.append(num)
#     print("是否继承输入? y为 继续,n为退出")
#     gameOver = input("功能选择:")
#     if gameOver == 'y':
#         continue
#     elif gameOver =='n':
#         print(list)
#         break
#     else:
#         print("输入功能有误，退出程序")
#         break

a = "1"
b = "1"
print(a is b)
print(id(a))
print(id(b))
print(a == b)

#  判断是否是回文数
num1 =num2 = int(input("请输入一个要判断的数字字符串:"))
t = 0
while num2 > 0:
    t = t*10 + num2 %10
    num2 = num2 // 10
if num1 == t:
    print("%s 是回文数"%num1)
else:
    print("%s 不是回文数"%num1)


# 比较运行符， 大小写转换。
# content = input("输入全字符的字符串信息:")
# str = ''
# for i in content:
#     if ('a'<=i<='z'):
#         char1 = ord(i) -32
#     elif ('A'<=i<='Z'):
#         char1 = ord(i)+32
#     else:
#         char1 = ord(i)+0
#     str += chr(char1)
# print("大小写转换:",str)

#  三个字符串排序
str1 = input("第一个字符串:")
str2 = input("第二个字符串:")
str3 = input("第三个字符串:")
print("排序之前的顺序: %s,%s,%s"%(str1,str2,str3))
if str1 >= str2:
    str1,str2 = str2,str1
if str1 >= str3:
    str1,str3 = str3,str1
if str2 >= str3:
    str2,str3= str3,str2
print("排序之后的顺序: %s,%s,%s"%(str1,str2,str3))
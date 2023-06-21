# list1 = [1,2,3,4]
# print("长度为:%d"%len(list1))
# print("第一个值是:%d"%list1[0])
# list1[0]=100
# print("设置新值后，第一个值是:{}".format(list1[0]))
# print("获取索引值:{}".format(list1.index(2)))

# 序列切片操作
list1 = [1,2,3,4,5,6,7]
print(list1[0:5])   # [1,2,3,4,5]
print(list1[4:6])    # [5,6]
print(list1[2:2])    # []
print(list1[-1:-3]) # []
print(list1[-3:-1]) #[5,6]

# 字符串切片
str = "Python"
print(str[:5])   # Pytho
print(str[2:])   # thon
print(str[-2:]) # on
print(str[:-3])  # Pyt
print(str[:])   # Python

# 元组切片
t = (1,2,3,4,5,6,7,8,9,10)
print(t[0:9:])  # (1,2,3,4,5,6,7,8,9)
print(t[0:9:2]) # (1,3,5,7,9)
print(t[0:9:4])  # (1,5,9)
print(t[::4])  # (1,5,9)
print(t[0:9:-2]) # ()
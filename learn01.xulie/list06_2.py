# 访问元素
list = [0,1,2,3,4]
print(list[2])
print(list[-1])
# 更新元素
list[2]= 200
print(list[2])
# 获取长度
print(len(list))
# 统计元素4出现的次数
print(list.count(4))
# 获取下标

# 调用 index 时， 注意变量名不能是 list
'''
list表示列表对象，参数value表示元素的值。
start和stop为可选参数，start表示起始检索的位置，包含start所在位置，
stop表示终止检索的位置，不包含stop所在的位置。
index()方法将在指定范围内，从左到右查找第一个匹配的元素，然后返回它的下标索引值
'''
list2 = [1,2,3,4,5,6,7]
print(list2.index(2,1,4))

#  遍历元素
list1 = [1,2,3,4,5,6]
i = 0
while i <len(list1):
    list1[i] = list1[i]+100
    i +=1
print(list1)  # [101, 102, 103, 104, 105, 106]

for i in list1:
    list1[list1.index(i)] = i +300
print(list1)   # [401, 402, 403, 404, 405, 406]

# 可以使用枚举， 变成 index, value
list2 = [1,2,3,4,5,6]
for index,value in enumerate(list2):
    list2[index] = value+500
print(list2)  # [501, 502, 503, 504, 505, 506]

list1 =[1,2,3]
# 添加元素
list1.append(4)
print(list1)  # [1, 2, 3, 4]


# 地址是一致的
a = [1,2,3]
print(id(a))  # 1873353031616
a = [2,3,4]
print(id(a)) # 1873352946816


a = [1,2,3]
b= [1,2,3]
print(a == b)  # True
print(id(a)==id(b)) # False
print(id(a[0]) ==id(b[0])) # True
print(id(a))   # 1873352946816
a.append(4)
print(id(a)) # 1873352946816


c = [1,2,3]
print(id(c)) # 2084896229760
c.extend((4,5,6))
print(c)  # [1, 2, 3, 4, 5, 6]
print(id(c)) # 2084896229760

# 插入元素  insert    insert(index,obj)
d= [1,2,3]
d.insert(0,4)
print(d)  # [4, 1, 2, 3]

# 删除元素 del
del d[1]
print(d)  # [4, 2, 3]

# pop 删除， 可以返回删除的元素
e = [1,2,3,4,5,6]
el1 = e.pop(-1)
print(e)  # [1, 2, 3, 4, 5]
print("删除的元素: %d" %el1)  # 6

el2 = e.pop(-2)
print(e)  # [1, 2, 3, 5]
print("删除的元素: %d" %el2)  # 4

# remove 移除， 首次出现
e.remove(1)
print(e)  # [2, 3, 5]

# 清空所有  clear
e.clear()
print(e) # []

'''
列表复制， 有浅复制和深复制
'''
import  copy
x = [1,2,[3,4]]
y = copy.copy(x)

# 浅复制，两个是一样的。
print(id(x[2]))  # 2100425881472
print(id(y[2])) #  2100425881472

z = copy.deepcopy(x)
print(id(x[2]) == id(z[2]))  # False

# 切片都是浅复制
d = x[:]
print(id(x[2]) == id(d[2]))  # True

# 删除整个列表
del x
print(x)   # NameError: name 'x' is not defined 








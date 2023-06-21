dict1 = {"x":1,"y":2,"z":3}
# 使用 [] 获取值
print(dict1["x"])   # 1
print(dict1["z"])  # 3
# 使用 get 获取值
print(dict1.get("x"))
print(dict1.get("a111","没有该值"))   #没有该值

# 遍历
for i in dict1:
    print("%s=%s" %(i,dict1.get(i)))
# x=1
# y=2
# z=3

# 通过key 进行遍历
for key in dict1.keys():
    print("%s=%s" %(key,dict1.get(key)))


# 遍历值
for va in dict1.values():
    print(va,end=" ")   # 1 2 3

print("\r\n")
# 遍历元素
for item in dict1.items():
    print(item,end="\r\n")

# ('x', 1)
# ('y', 2)
# ('z', 3)

# 添加值
dict1['a1'] = 3
dict1['name']= 'zhangsan'
dict1['x']=100
print(dict1)

# {'x': 100, 'y': 2, 'z': 3, 'a1': 3, 'name': 'zhangsan'}

# setdefault(key,default=None)  设置值，有key 返回原先的，没有key 则为默认值
newValue = dict1.setdefault('x',200)
print("打印值: %s" %newValue)  # 打印值: 100


# 删除 元素  del
del dict1["x"]
del dict1["y"]
print(dict1)   # {'z': 3, 'a1': 3, 'name': 'zhangsan'}

# pop (key,default) 根据key删除， 返回原先的值，没有key的话，返回默认值.
newValue1 = dict1.pop("z","默认值")
newValue2 = dict1.pop("x","默认值")
print(dict1)
print("打印值: %s,%s" %(newValue1,newValue2))   # 打印值: 3,默认值

# popitem() 随机删除一个元素， 如果没有元素了，调用该方法，则抛出 KeyError 异常
dict1.popitem()
print(dict1)  # {'a1': 3}

# 清理 clear
dict1.clear()
print(dict1)  # {}

# in 检测项目是否存在
str = input("请输入要统计的字符串:")
dic2 = dict()
for cha in str:
    if cha in dic2:
        dic2[cha] +=1
    else:
        dic2[cha] =1
for key in dic2:
    print("%s=%d," %(key,dic2.get(key)), end= " ")






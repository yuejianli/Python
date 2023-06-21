'''
tuple 元组 不可变序列
用  () 小括号表示, 没有添加，删除，更新方法。

小括号不是必须的。
'''

t1 = (1,2,3)
print(t1)

#  一. 格式化输出
name = "zhangsan"
sex = "男"
print("普通打印: %s 是 %s" %(name,sex))
up = (name,sex)
print("元组打印: %s 是 %s" %up)

#  多重赋值

a =1
b =2
a,b = b,a
print("a= %s,b=%s" %(a,b))

# 与 list 转换

list1 = [1,2,3,4]
up = tuple(list1)
print(up)  # (1, 2, 3, 4)
print(list(up))  # [1, 2, 3, 4]



# zip 表示压缩
a = [1,2,3]
b = [4,5,6]
c = zip(a,b)
print(list(c)) # [(1,4), (2,5), (3,6)]

# 长度不一样，以最少的为准
a = [1,2,3]
b = [4,5,6,7]
c = zip(a,b)
print(list(c))  #  [(1, 4), (2, 5), (3, 6)]

#  *zip 进行解压

a1 = [1,2,3]
b1 = [4,5,6]
c1 = [7,8,9,10]
c = zip(a1,b1,c1)
# print(list(c))   #  中间不能打印， 否则解压缩会出错。 [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# 进行解压， 给3个序列
a2,b2,c2 =zip (*c)
print(list(a2))
print(list(b2))
print(list(c2))


# 枚举函数 enumerate(seq, start =0) 常用于for 循环中
list1 = ['a','b','c','b','d']
enum = enumerate(list1)
# 打印
print(list(enum))

# 会打印出 下标和值， 并不会去重。 会按照列表的顺序进行枚举。
#  [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'b'), (4, 'd')]

for index,value in enumerate(list1):
    # 转换成大写
    list1[index] = value.upper();
print(list1)            #   ['A', 'B', 'C', 'B', 'D']

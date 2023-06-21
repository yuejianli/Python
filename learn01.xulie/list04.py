# 进行排序
'''

➢　sequence.reverse()：翻转顺序。直接在调用对象上改动，没有返回值，因此不可变对象不能调用。
➢　reversed(sequence)：翻转顺序。返回翻转后的序列对象。➢　
sequence.sort()：自定义排序。直接在调用对象上改动，没有返回值，因此不可变对象不能调用。
➢　sorted(sequence)：自定义排序。返回排序后的序列对象。

'''

a = [1,2,3,4]
a.reverse()
print(a)

r = [1,2,3,4]
# reversed 返回的是一个序列， 要用 list() 包含里面
print(list(reversed(r)))

# 排序   sorted(sequcne, key,reverse)

a = [5,2,3,1,4]
a.sort()
print(a)   # 排序  [1,2,3,4,5]

b = [1,2,5,2,4,3]
# 倒序
print(list(sorted(b,reverse=True)))


str1 = " This is a test string from Python"
# 定义两个数组，按照 空格进行拆分
str2 = sorted(str1.split())
str3 = sorted(str1.split(),key = str.lower)
print(list(str2))   #  ['Python', 'This', 'a', 'from', 'is', 'string', 'test']
print(list(str3))   # ['a', 'from', 'is', 'Python', 'string', 'test', 'This']

# 数组排序
scores = [
    ('zhangsan','A',95),
    ('list','B',85),
    ('wangwu','B',80)
]

# 进行排序，按照成绩
l2 = sorted(scores,key= lambda t:t[2],reverse=True)
print(list(l2))   #  [('zhangsan', 'A', 95), ('list', 'B', 85), ('wangwu', 'B', 80)]




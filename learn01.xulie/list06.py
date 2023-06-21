'''
列表  [元素1，元素2]

'''

list1 = list((1,2,3))
print(list1)   # [1, 2, 3]

# 字符串样式
list2 = list("Python")
print(list2) # ['P', 'y', 't', 'h', 'o', 'n']

# 字典   ['x', 'y', 'z']
list3 = list({'x':1,'y':2,'z':3})
print(list3)

# 空列表
list4 = list()
print(list4)  # []

'''
列表推导式:

[expr for value in interable if condition]

类似于:

result = []
for value in interable:
    if condition:
        result.append(expr)
'''


L = [i for i in range(0,10) if 1==1]
print(L)   #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

L1= [i*i for i in range(1,4)]
print(L1)   # [1, 4, 9]


L = [[i,char] for i,char in enumerate("Python")]
print(L)   #  [[0, 'P'], [1, 'y'], [2, 't'], [3, 'h'], [4, 'o'], [5, 'n']]

L = [[0]*3 for i in range(3)]
print(L)   # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

'''
可以在 for 循环前面加  if-else 也可以在后面加 if -else
'''

L = [i if i %2 ==0 else 0 for i in range (10)]   #  [0, 0, 2, 0, 4, 0, 6, 0, 8, 0]
print(L)

L = [i for i in range(10) if i %2 ==0]
print(L)   # [0, 2, 4, 6, 8]






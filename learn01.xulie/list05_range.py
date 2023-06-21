'''
range 不可变的数字序列

range (start,stop,step)
'''

print(list(range(4)))  # [0, 1, 2, 3]
print(list(range(1,4)))  # [1, 2, 3]
print(list(range(1,4,2)))  #  [1, 3]
print(list(range(0,-5,-1)))  # [0, -1, -2, -3, -4]
print(list(range(0)))  # []
print(list(range(1,0))) # []

# 具有序列的相应的功能
r = range(1,10,2)
print(list(r))  # [1, 3, 5, 7, 9]
print(len(r)) # 5
print(3 in r) # True

'''
判断相等， 长度相同，包含的元素也相同，即表示相同
'''

print(range(0,3,2) == range(0,4,2))  #  True
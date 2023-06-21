#  加法计算
list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2)

# 乘法

list1 = [1,2,3]
print(list1 *3) # [1,2,3,1,2,3,1,2,3]
print(list1 * -2) # []

# 被多次引用
list3 = [[]]
list4 = list3 * 3
list4[0].append(3)
print(list4)   # [[3],[3],[3]]

# 最大值，最小值和 和
print(max(list1))
print(min(list1))
print(sum(list1))


# 成员检测，  in not in
a = [1,2,3]
print(1 in a)  # True
b = [[1],[2],[3]]
print( 1 in b) # False
str = "Python"
print('n' in str)  # True

# 去重

a = [1,2,3,1,2,3,4,5,1,2]
b = []
for i in a:
    if i not in b:
        b.append(i)
print("去重后的数组为:",b)

# any all  any 有一个元素为真则为 True   all 全部为真才为 True
a = [1,2,"",0]
print(any(a))  # True
print(all(a))   # False


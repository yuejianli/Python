
# 1. 把字典格式转换为列表表示形式

dict2 = {"x":1,"y":2,"z":3}
list = [(k+':') for k,v in dict2.items()]
print(list)

# 2. 过滤长度小于3的字符串列表，并将剩下的转换成大写字母

names = ["Bob","Tom","Jerry","Smith"]
l = [name.upper() for name in names if len(name) >3]
print(l)    # ['JERRY', 'SMITH']

# 3. 求(x,y)，其中，x是0~5之间的偶数，y是0～5之间的奇数组成元组的列表
l = [(x,y) for x in range(5) if x %2==0 for y in range(5) if y%2 !=0]
print(l)    # [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]



# 进制转换， 转换成 二进制

# 定义函数
def d2b(num):
    a = []
    result = ''
    while num > 0:
        yu = num % 2
        a.append(yu)
        num = num//2
    # 倒序连接
    while (len(a)):
        result += str(a.pop())
    return "0b" +result

# 调用函数
print(d2b(10))
print(d2b(12))

# 游戏

'''
有一群猴子排成一圈，按1、2、3、…、n依次编号。然后从第1只开始数，数到第m只，则把它踢出圈，
然后从它后面再开始数，当再次数到第m只时，继续把它踢出去，
依此类推，直到只剩下一只猴子为止，那只猴子就叫作大王。
要求编程模拟此过程，输入m、n，输出最后那个大王的编号。
这里主要运用队列运算。队列运算遵循先进先出、后进后出的原则。
定义一个函数，接收两个参数：n表示猴子个数，m表示踢出位置。
函数返回值为最后一个剩余猴子的索引号
'''

def game (n,m):
    arr = []
    for i in range (1, n+1):
        arr.append(i)
    # 列表只剩下一个时退出循环:
    while (len(arr) > 1):
       for i in range(m-1):
           # 追加到后面去
            arr.append(arr.pop(0))
       # 移除对应的 m个位置。
       arr.pop(0)
    return arr[0]

print(game(5,3))


#  将元组转换成对象处理， 通常是固定数目的处理， 如点， 有 横，纵坐标两个位置。

a = (1,2)
print(a[0])

from collections import namedtuple
Point = namedtuple("Point",["x","y"])
p = Point(1,2)
# 通过 p.x  p.y 进行打印
print(p.x)
print(p.y)

# 双向队列 deque
'''
双向队列 deque

➢　append(x)：添加x到右端。
➢　appendleft(x)：添加x到左端。
➢　extend(iterable)：在队列右侧添加iterable中的元素。
➢　extendleft(iterable)：在队列左侧反序添加iterable中的元素。
➢　pop()：移除最右侧的元素。
➢　popleft()：移除最左侧的元素。
'''
from collections import deque
d = deque(maxlen= 10)
d.append(1)
d.extendleft(range(9))  # deque([8, 7, 6, 5, 4, 3, 2, 1, 0, 1], maxlen=10)
print(d)

#  判断是否是回文
from collections import deque
def huiwen (strText):
    d = deque()
    for i in strText:
        d.append(i)
    huiwen = True
    while (len(d) >1 and huiwen):
        start = d.popleft()
        end = d.pop()
        if (end != start):
            huiwen = False
    return huiwen
str = "abcde"
print(huiwen(str))  #  False
str = "abcba"
print(huiwen(str))  # True


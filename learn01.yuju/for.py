#  打印水仙花数
# print("1000以内的水仙花数是:\r\n")
# for i in range (100,1000):
#     ge = i %10
#     shi = (i//10) %10
#     bai = i//100
#     if i == (ge**3 + shi **3 + bai**3):
#         print(" %s\r" %i)

# 打印 2 ~ 100 以内的质数
# for i in range (2,101):
#     zhishu = True
#     for j in range(2,i):
#         if (i%j == 0):
#             zhishu = False
#             break;
#     if (zhishu):
#         print(i,end=" ")

# 组成不重复的数字
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j and j!= k and i!=k):
                print((i*100+j*10+k),end=" ")
                count+=1
print("\r\n总数是:",count)

'''
break 和 continue  退出循环
'''

#  找到所有的 int 类型的数据

a = [1,2,3,"a","c",3.2,4.2]
b=[]
for i in a:
    if (not isinstance(i,int)):
        continue
    b.append(i)
print(b)
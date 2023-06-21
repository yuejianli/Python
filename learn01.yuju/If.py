# 随机生成一个数，看是偶数不
# import random
# # 随机生成1 ~100的整数
# num = random.randint(1,100)
# if num %2 == 0:
#     print("%s 是偶数"%num)

year = int(input("请输入年份:"))
if ( (year %4 == 0 and year %100 !=0) or (year %400 ==0)):
    print("%s 是闰年" %year)
else:
    print("%s 不是闰年" %year)


'''

➢　a说："我不是小偷。"
➢　b说："c是小偷。"
➢　c说："小偷肯定是d。"
➢　d说："c胡说！"
'''
# for i in range (1,5):
#     if ((i!=1)+(i==3)+(i==4)+(i!=4)) == 3:
#         str = chr(i+96)
#         break
# print("%s 是小偷"%str)

'''
假设有一个小球，从100 m高空自由落下，每次落地后反跳回原高度的一半再落下，求当小球第10次落地时，共运行了多少米，第10次反弹的高度是多少？
'''

# sum = 0
# height = 100
# num = 10
# for i in range (1,num+1):
#     if i == 1:
#         sum = height
#     else:
#         sum += height /2
#     height/=2
# print("共运行 {} 米".format(sum))
# print("第 10次高度是 {}".format(height))


#  成绩验证
# score = int(input("请输入成绩:"))
# if score < 0 or score > 100:
#     print("成绩不符合规范")
# else:
#     if score < 60:
#         print("不合格")
#     elif score < 70:
#         print("刚及格")
#     elif score < 80:
#         print("中")
#     elif score < 90:
#         print("良")
#     else:
#         print("优秀")

'''
【示例2】假设某城市的出租车计费方式为：起步2km内5元，2km以上每千米收费1.3元，9km以上每千米收费2元，不足1km的算1km，燃油附加费1元。编写程序，输入距离，计算所需的出租车费用
'''

# import  math
# km = math.ceil(int(input("请输入运行公里数:")))
# money = 1
# if km <=2 :
#     money += 5
# elif km<=9:
#     money = money+5+(km-2)*1.3
# else:
#     money = money +5 +(9-2)*1.3 + (km-9)*2
# print("跑了 {} 公里，需要打车钱 {}".format(km,money))

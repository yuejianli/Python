# 进度条展示处理
# import time  # 导入time模块
# length = 100
# for i in (1,length+1):
#     #计算百分比
#     percentage = i / length
#     # 处理个数
#     block = "#" * int(i//5)
#     # 休眠
#     time.sleep(1)
#     # 打印信息:
#     print("\r\n 加载进度条: | {} | {}".format(block,percentage))

# 统计列表中总分，最大值和优秀值
# scores = {
#     "张三":89,
#     "李四":80,
#     "王五":95,
#     "赵六":64
# }
# sum = 0
# maxScore = 0
# maxName = ''
# print("语文优秀生名单:")
# for i in scores:
#     sum += scores[i]
#     if scores[i] >= 85:
#         print("优秀生: %s,%.2f" %(i,scores[i]))
#     if maxScore < scores[i]:
#         maxScore = scores[i]
#         maxName = i
# print("\r\n")
# print("语文平均分是: %s"%(sum/len(scores)))
# print("语文最高分是: %s, 姓名是: %s"%(maxScore,maxName))

# 计算被 9 整除的数字
# num1 = int(input("请输入要被整除的数字，末尾是3或者9:"))
# count = 1
# canDiv = False
# startNum = 9
# while not canDiv:
#     if startNum % num1 == 0:
#         canDiv = True
#         break
#     else:
#         startNum *= 10
#         startNum += 9
#         count+=1
# print("{} 个9 可以被 {} 整除".format(count, num1))
# r = startNum // num1
# print("{}/{}={}".format(startNum,num1,r))


# 数字计算器
print("进行一个简单的四则运算")
while True:
    x = int(input("第一个值:"))
    op = input("输入操作符: [+ - * / %]:")
    y = int(input("第二个值:"))
    operator = {
        "+":x+y,
        "-":x-y,
        "*": x*y,
        "/": x/y,
        "%": x %y
    }
    result  = operator.get(op)
    print("{} {} {} = {}".format(x,op,y,result))
    ok = input("是否继续游戏 [y,n]:")
    if ok == 'y':
        continue
    elif ok == 'n':
        print("游戏结束:")
        break
    else:
        print("功能选择错误,游戏结束:")
        break

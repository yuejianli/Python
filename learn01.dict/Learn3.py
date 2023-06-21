#  update 字典更新
dict1 = {"x":1,"y":2,"z":3}

# update() 更新， 如果有，则更新，没有，则添加

dict2 = {"a":1,"b":1}
dict1.update(e='3')
dict1.update(dict2)
dict1.update([("f",4)])
print(dict1)    # {'x': 1, 'y': 2, 'z': 3, 'e': '3', 'a': 1, 'b': 1, 'f': 4}

#  合并    d = d | other   d |= other

dict3 = {"x":1,"y":2,"z":3}
dict3 |= dict2
print(dict3)   # {'x': 1, 'y': 2, 'z': 3, 'a': 1, 'b': 1}


# 复制
dict4 = {"x":1,"y":2,"z":3, "arr":[2,3,4]}
dict5 = dict4.copy()
print(id(dict4["arr"]) == id(dict5["arr"]))   # True

# 深复制
import copy
dict6 = copy.deepcopy(dict4)
print(id(dict4["arr"]) == id(dict6["arr"]))   # False

# 删除字典  del
print("del 进行删除字典操作 \r\n")
print(dict6)
del dict6
# print(dict6)  # name 'dict6' is not defined. Did you mean: 'dict1'?


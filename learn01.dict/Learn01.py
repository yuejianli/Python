dict1 = { "x":1,"y":2,"z":3}
print(dict1)
dict2 = {}
print(dict2)

t1 = ("x","y","z")
t2 = (1,2,3)
d = dict(zip(t1,t2))
print(d)   # {'x': 1, 'y': 2, 'z': 3}

dict3 = dict(x=1,y="2",z="3.0")
print(dict3)   # {'x': 1, 'y': '2', 'z': '3.0'}

dict4 = dict([("x",1),("y",2),("z",3)])
print(dict4)  # {'x': 1, 'y': 2, 'z': 3}

enu1 = enumerate([1,2,3])
dict5 = dict(enu1)
print(dict5)   # {0: 1, 1: 2, 2: 3}


dict6 = dict.fromkeys(range(6),False)
print(dict6)   # {0: False, 1: False, 2: False, 3: False, 4: False, 5: False}


'''
字典推导式:

{键：值 for 一个/组变量 in 可迭代对象  if 条件表达式}

'''
a = {'a':1,'b':2,'c':3,'A':4,'B':5}
b = {k:v for k,v in a.items()}
print(b)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

c = {k.lower() : a.get(k.lower(),0) +a.get(k.upper(),0) for k in a.keys() if k.lower() in ['a','b']}
print(c)   # {'a': 5, 'b': 7}








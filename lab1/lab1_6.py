from collections import defaultdict

d=defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d=defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

'''defaultdict
会自动为将要访问的键
（就算目前字典中并不存在这样的键）
创建映射实体。 如果你并不需要这样的特性，
你可以在一个普通的字典上
使用 setdefault() 方法来代替'''
d={}#importante  每次都要创建空链表
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)


##further
d={}
pairs={'a':1,'b':2}
for key, value in pairs.items():

    if key not in d:
        d[key] = []
    d[key].append(value)
print(">>>>")
print(d)

# #-->
# d={'a':'1','b':'1'}
# for key in d:
#     print(key)
# for key,value in d.items():
#     print(key,value)
d=defaultdict(list)
pairs={'a':1,'b':2}
for key,value in pairs.items():
    d[key].append(value)
print(d)

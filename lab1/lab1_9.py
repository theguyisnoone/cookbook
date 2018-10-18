a={
'x':'1',
'y':'2',
'z':'3'
}
b={
'w':'10',
'x':'11',
'y':'2',

}

#find keys in common
print(a.keys()&b.keys())
#find keys in a  that are not  in b
print(a.keys()-b.keys())# '''如果a有b的全部元素 输出set()'''
#find (key,value) in common
print(a.items()&b.items())

print(">>>>>")
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)

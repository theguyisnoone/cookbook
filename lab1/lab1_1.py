"""title:解压序列赋值给多个变量 """
"""Q:现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后
同时赋值给 N 个变量？"""

p=(4,5)
x,y=p
print(f"x:{x} y:{y}")


data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
a,b,c,d=data
print(f"{a} {b} {c} {d}")

''' data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
 a,b,c=data
 print(f"{a} {b} {c} {d}")'''
#Traceback (most recent call last):
# File ".\lab1_1.py", line 15, in <module>
#    a,b,c=data
# ValueError: too many values to unpack (expected 3)
###实验二解决了这个问题

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_,_,_,d=data #取出个别 ！！   importante

print(f"{d}")

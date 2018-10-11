'''解压可迭代对象赋值给多个变量
问题 '''

#test
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name,email,*phone_number=record
print("name:{},email:{},phone_number:{}".format(name,email,phone_number))
#console!!!
# name:Dave,email:dave@example.com,phone_number:['773-555-1212', '847-555-1212']

class test(object):
    def drop_first_last(self,grades):
        first,*middle,last=grades
        avg=sum(middle)/len(middle)
        print("avg without first and last:{}".format(avg))


grades=(66,77,43,99,95)
t1=test()
t1.drop_first_last(grades)

#扩展 可变长元组
records =[('foo',1,2),('bar','hello'),('foo',3,4)]
#[(tag,*args),(...),(...)]
def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records: #def 写在前面 不然找不到
    if tag =='foo':
        do_foo(*args)
    else:
        do_bar(*args)


#字符串分割
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*field,homedir,sh=line.split(':')
print("uname:{},field:{},homedir:{},sh:{}".format(uname,field,homedir,sh))


#使用一个普通的废弃名称 解压一些元素并丢弃他们
record = ('ACME', 50, 123.45, (12, 18, 2012))
name,*_,(*_,year)=record
print(name)
print(year)

#用分割语法去巧妙的实现递归
items=[1, 10, 7, 4, 5, 9]
head,*tail=items
print(head,tail)
def sum(items):
    head,*tail =items
    return head +sum(tail) if tail  else head

print(sum(items))

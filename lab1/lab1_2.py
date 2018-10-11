'''解压可迭代对象赋值给多个变量
问题 '''
class test(object):
    def drop_first_last(self,grades):
        first,*middle,last=grades
        avg=sum(middle)/len(middle)
        print("avg without first and last:{}".format(avg))

#test
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name,email,*phone_number=record
print("name:{},email:{},phone_number:{}".format(name,email,phone_number))
#console!!!
# name:Dave,email:dave@example.com,phone_number:['773-555-1212', '847-555-1212']



grades=(66,77,43,99,95)
t1=test()
t1.drop_first_last(grades)

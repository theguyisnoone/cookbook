'''解压可迭代对象赋值给多个变量
问题 '''
# import math
# def drop_first_last(grades):
#     first,*middle,last=grades
#     return avg(middle)#去除第一个和最后一个的平均值

#test
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name,email,*phone_number=record
print("name:{},email:{},phone_number:{}".format(name,email,phone_number))
#console!!!
# name:Dave,email:dave@example.com,phone_number:['773-555-1212', '847-555-1212']



# grades=(66,77,43,99,95)
# print(drop_first_last(record)) #avg不是自带函数

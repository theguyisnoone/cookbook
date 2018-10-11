import heapq
class PriorityQueue:
    def __init__(self):
        self._queue=[] #null
        self._index=0#null

    def push(self,item,priority):
        heapq.heappush(self._queue, (-priority,self._index,item)) #？、
        self._index+=1

    def pop(self):
        return  heapq.heappop(self._queue)[-1]#min？


class Item:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

# q=PriorityQueue()
# q.push(Item('foo'), 1)
# q.push(Item('bar'), 5)
# q.push(Item('spam'),4)
# q.push(Item('gork'),1)
# print(q.pop())
# # Item('bar')
# print(q.pop())
# # Item('spam')
# print(q.pop())
# # Item('foo')
# print(q.pop())
# # Item('gork')
#
# print(q.pop())



'''verification'''
'''只使用二元组（优先级，item） only diff priority'''
a=(1,Item('xxx'))
b=(2,Item('xdsd'))
print(a<b) #True
# c=(1,Item('ZZZZZ'))
# print(a<c)#error!

'''(priority,index,item)''''
x=(1,0,Item('q'))
y=(1,1,Item('z'))
print(x<y)

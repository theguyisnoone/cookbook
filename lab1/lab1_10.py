def dedupe(items):
    seen=set()
    for item  in items:
        if item not in seen:
            yield item#yield
            seen.add(item)

a=[1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
# [1, 5, 2, 9, 10]

#develop  消除元素不可哈希（比如 dict 类型）
# 的序列中重复元素的话
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a,key=lambda d: (d['x'],d['y']))))
print(list(dedupe(a,key=lambda d: d['x'])))

#further
'''如果只想消除元素'''
a=[1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))
#没有保持原排序
# {1, 2, 5, 9, 10}

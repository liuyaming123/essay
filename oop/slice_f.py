# -*- coding:utf-8 -*-

"""slice原理"""


class Demo:
    def __getitem__(self, item):
        return item, type(item)


d = Demo()
print(d[1])  # 1
print(d[1:4])  # slice(1, 4, None)
print(d[1:4:2])  # slice(1, 4, 2)
print(d[1:4:2, 3])  # (slice(1, 4, 2), 3)
print(d[1:4:2, 3:5])  # (slice(1, 4, 2), slice(3, 5, None))

# slice类本身如何处理切片
'''
>>> slice
<class 'slice'>
 # 为了省事，截取最后的属性
>>> dir(slice)[-4:]
['indices', 'start', 'step', 'stop']



>>> help(slice.indices)
Help on method_descriptor:
indices(...)
    S.indices(len) -> (start, stop, stride)
    
    Assuming a sequence of length len, calculate the start and stop
    indices, and the stride length of the extended slice described by
    S. Out of bounds indices are clipped in a manner consistent with the
    handling of normal slices.


例如： 
"abcde"[:10:2], 但"abcde"的长度只有5，索引end = 10，超出了"abcde"的长度范围。因此会内部调用indices，处理超出边界的索引。
因此，"abcde"[:10:2]就会被内部处理变成"abcde"[0:5:2]。

1. Python内部处理时，会生成一个slice(0, 10, 2)
2. 然后使用slice(0, 10, 2).indices(len("abcde"))得到(0,5,2)，即start, end ,stride三个slice属性
3. 最后调用"abcde"[0:5:2]得到切片的字符串"ace"
'''

# -*- coding:utf-8 -*-
# python3.7.5

from functools import reduce
import sys
import os
import random
import time
import redis


a = map(lambda x: 5 * x, [1, '2', 3])
b = reduce(lambda x, y: x * y, [1, '2', 3])

# print(a)  # 返回map对象
# print(list(a))

# print('hello')
# sys.exit('programming exit!')
# print('python')


# sys.argv 获取命令行参数，返回值是List，第一个元素是程序本身
# # c = sys.argv[1]

os.path.abspath('abc.py')  # 返回该文件的绝对路径

# with open('asyncio_f.py', 'r') as f:
#     lines = f.readlines()
#     for i in lines:
#         if len(i) < 10:
#             continue
#         print(i.strip().strip())


# lambda 配合sorted排序
f = [('f', 5), ('d', 7), ('w', 3), ('r', 6), ('c', 4), ]
g = sorted(f, key=lambda x: x[0], reverse=True)
print(g)

'''
Python 切片[::-1]操作序列翻转
b = a[i:j:s]:

i为起始索引(缺省为0)，
j为结束索引(不包括，缺省为len(a))，
s为步进(缺省为1).

所以a[i:j:1]相当于a[i:j].

 
当s<0时:
i缺省时，默认为-1，
j缺省时，默认为-len(a)-1，

所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍。
'''

# =================================================================================================
# python-redis的pipeline使用方法
# from concurrent.futures import ProcessPoolExecutor
#
# r = redis.Redis(host='10.93.84.53', port=6379, password='bigdata123')
#
#
# def try_pipeline():
#     start = time.time()
#     with r.pipeline(transaction=False) as p:
#         p.sadd('seta', 1).sadd('seta', 2).srem('seta', 2).lpush('lista', 1).lrange('lista', 0, -1)
#         p.execute()
#     print(time.time() - start)
#
#
# def without_pipeline():
#     start = time.time()
#     r.sadd('seta', 1)
#     r.sadd('seta', 2)
#     r.srem('seta', 2)
#     r.lpush('lista', 1)
#     r.lrange('lista', 0, -1)
#     print(time.time() - start)
#
#
# def worker():
#     while True:
#         try_pipeline()
#
# with ProcessPoolExecutor(max_workers=12) as pool:
#     for _ in range(10):
#         pool.submit(worker)

# =================================================================================================

# host="r-uf611193d98371b4.redis.rds.aliyuncs.com",port=6379,db=40,password="D22f408c"
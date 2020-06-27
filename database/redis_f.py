# -*- coding:utf-8 -*-
"""redis python测试"""

import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

'''string写入'''
# r.set('s_age', 100, 20)
# r.mset(dict(host='localhost', port=6379, db=0))

'''hash写入'''
# r.hset('h_liu', 'name', 'liuyaming'),  # 单个kv写入
# r.hmset('h_liu', dict(name='lym', age=20, sex=1))  # 多个kv写入

'''list写入'''
# li = [11, 22, 33, 44, 55, 'aa', 'bb', 'cc']
# r.rpush('l_name', *li)

'''set写入'''
# li = [1, 1, 2, 2, 4, 4, 5, 5, 5, 5]
# r.sadd('se_x', *li)  # 多个写
# r.sadd('se_x', 9)  # 单个写

print(
    # -------> string操作
    # r.keys(),
    # r.get('s_name'),

    # -------> hash操作
    # r.hgetall('h_hyy'),
    # r.hlen('h_hyy'),

    # r.smembers('se_x'),
    # r.lrange('l_name', 0, 2)
)

# -*- coding:utf-8 -*-
# 协程
# 因为协程是一个线程执行，那怎么利用多核CPU呢？
# 最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。


# =========================================================================
# 生产者消费者模型
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
#
# c = consumer()
# produce(c)


# =========================================================================
# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持
# asyncio的编程模型就是一个消息循环。从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO
import threading
import asyncio


@asyncio.coroutine  # 把generator标记为coroutine类型
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello(), hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# ==========================================================================














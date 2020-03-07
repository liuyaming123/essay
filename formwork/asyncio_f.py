# -*- coding:utf-8 -*-
# async.py  python单线程执行异步任务

import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)   # 一个任务阻塞的时候其他会执行
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())

asyncio.run(main())



# 在 async 函数main的里面，asyncio.gather() 方法将多个异步任务（三个 count()）包装成一个新的异步任务，
# 必须等到内部的多个异步任务都执行结束，这个新的异步任务才会结束

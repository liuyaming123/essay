# -*- coding:utf-8 -*-


# 基本装饰器
# def A(fun):
#     print("we are feel good!")
#     fun()
#     print("sincerely.")
#     return lambda: None
#
#
# @A
# def B():
#     print("B")


# 带参数的装饰器，本质上就是一个闭包函数
def wraper(fun):
    def inner(*args, **kwargs):
        print("执行函数前要处理的")
        fun(*args, **kwargs)
        print("执行函数后要处理的")
        return fun
    return inner


@wraper
def E(name, age):
    print('my name is %s, age is %s' % (name, age))


E("Jane", 1)

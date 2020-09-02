# -*- coding:utf-8 -*-
"""decorator"""


# 闭包：内部函数调用外部函数的局部变量，外部函数返回内部函数的函数名
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
#
#
# print(outer(1)(5))


# -------------------------------------------------------------------


# 装饰器本身不带参数
# def outer(func):
#     def inner(*args, **kwargs):
#         print('被装饰函数执行前执行')
#         func(*args, **kwargs)
#         print('被装饰函数执行后执行')
#     return inner
#
#
# @outer
# def peak(a, b, sex='男'):
#     print(a, b, sex)
#
#
# peak(3, 5)


# -------------------------------------------------------------------


# 装饰器本身带参数
def wrapper(max_times=5):
    def outer(func):
        def inner(*args, **kwargs):
            for i in range(max_times):
                try:
                    func(*args, **kwargs)
                    break
                except Exception as e:
                    print(e)
        return inner
    return outer


@wrapper(max_times=2)
def peak_of_life(a, b):
    r = a / b
    print(r)


peak_of_life(1, 2)


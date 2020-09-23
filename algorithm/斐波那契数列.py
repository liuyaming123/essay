# -*- coding:utf-8 -*-
"""使用生成器生成斐波那契数列的前n项"""


def fb(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


for i in fb(10):
    print(i)

# -*- coding:utf-8 -*-
# 钻石继承问题（菱形继承）


# class A:
#     def __init__(self):
#         print('A')
#
#
# class B(A):
#     def __init__(self):
#         print('B')
#         A.__init__(self)
#
#
# class C(A):
#     def __init__(self):
#         print('C')
#         A.__init__(self)
#
#
# class D(B, C):
#     def __init__(self):
#         print('D')
#         B.__init__(self)
#         C.__init__(self)


# d = D()  # 结果：D B A C A  一个菱形继承出现了两次 A，浪费资源，内存


# super()解决：
class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


class C(A):
    def __init__(self):
        print('C')
        super().__init__()


class D(B, C):
    def __init__(self):
        print('D')
        super().__init__()


d = D()
'''
D
B
C
A
'''


# 每个类都有一个mro属性，它的值是一个元组，按照方法解析顺序（Method Resolution Order, MRO）列出各个超类
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

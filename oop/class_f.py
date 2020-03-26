# -*- coding:utf-8 -*-
abc = '类和对象的理解'

'''
对象创建的过程：
创建对象：同时创建了3个对象--->
1.元对象  class---创建元对象
2.类对象  在编译（或解释）时创建
3.实例对象
'''


'''
self:
    1.self 指代当前对象，谁调用方法谁就是当前对象
    2.self变量名可以修改，本质上只是一个位置参数
    3.self被传递进来的是外面的对象的地址（引用）
'''


# 类属性：定义在类之内，任何方法之外的变量
# 实例属性：**定义在方法之内的属性**
# 在类里边调用属性的形式：self.属性名


class Student:
    # 类属性
    name = '小明'
    age = 17
    sex = 'male'
    id = '007'

    def __init__(self):  # 魔法方法---初始化方法---构造方法   构造方法里的参数：构造参数
        print('this is init')
        # 构造方法默认return None，也必须返回None

    # 类方法
    def learn(self):
        '''
        self: 指代当前对象(谁调用这个方法谁就是当前对象) ～本质上只是一个位置参数，可以修改
        self: s1调用，self = s1，引用--相同---修改的是同一个对象
        '''
        self.name = '小黑'  # 实例属性,在这里遮蔽类属性
        # name = 'he'  # 局部变量

        print(self)  # self: <__main__.Student object at 0x10df84b90>
        print(self.name)  # self.名字--->调用属性（可以是类属性，也可以是实例属性）
        pass

    @staticmethod
    def eat():
        print('I can eat')


s1 = Student()
s2 = Student()

s1.learn()  # 改名--->实例属性-->和类属性名字一样-->覆盖类属性
print(s1.name, s2.name)


# -*- coding:utf-8 -*-
# python私有化，只是改了名字（伪私有化）


class Card:
    """this is a card class"""
    __pwd = '123'  # 类属性前加两条下划线表示私有化

    def get_pwd(self):
        return self.__pwd

    def set_pwd(self, new_pwd):
        self.__pwd = new_pwd
        return self.__pwd


c = Card()
# print(c.__pwd)  # 私有化的类属性不能直接被类访问
# print(c._Card__pwd)  # 可以通过_类名+私有属性名访问
print(c.get_pwd())
c.set_pwd('789')
print(c.get_pwd())

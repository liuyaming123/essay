# -*- coding:utf-8 -*-
abc = '组合'


'''
组合：
    ***如果一个类的属性是一个对象，则称为组合***
'''


class Student:
    age = 6


class Teacher:
    salary = 99999


class School:
    s = Student()
    t = Teacher()

    def attend_class(self):
        print(self.t)
        print('学生到校上课，老师到校讲课')


sch = School()
sch.attend_class()
print(sch.t.salary)
print(sch.s.age)

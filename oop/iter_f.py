# -*- coding:utf-8 -*-
"""实现可迭代对象"""

'''
可迭代的对象 和 迭代器的区别：
可迭代的对象有个 __irer__ 方法，每次都实例化一个新的迭代器；
而迭代器要实现 __next__ 方法，返回单个元素，此外还要实现 __iter__ 方法，返回迭代器本身
'''

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


if __name__ == '__main__':
    s = Sentence('i love ShangHai')
    for i in s:
        print(i)

    print(type(s))  # <class '__main__.Sentence'>

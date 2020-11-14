# -*- coding:utf-8 -*-
"""列表实现栈的ADT --抽象数据类型"""


class Empty(Exception):
    pass


class ListStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('stack is empty.')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty.')
        return self._data.pop()


# S = ListStack()
# S.push(5)
# S.push(8)
# print(S.top())
# print(len(S))
# print(S.pop())
# print(S.is_empty())
# print(S.pop())
# print(S.is_empty())


# --------------------------------------------------------------------------------
# 栈的应用
# 判断表达式当中的大、中、小括号是否匹配

lis = [
    '()(()){([])}',  # 正确
    '((()(()){([()])}))',  # 正确
    ')(())',  # 错误
    '({[])}',  # 错误
    '('  # 错误
]


#  判断是否先出现左边的，是，保存在栈，继续，否则不匹配
#  判断每一个出现的右边与最后一个左边（栈顶元素）是否对称，如果对称，删除最后一个左边，否则不匹配
#  最终判断栈是否为空


def is_matched(s):
    left = '([{'
    right = ')]}'
    li = []
    for i in s:
        if i in left:
            li.append(i)
        elif i in right:
            if len(li) == 0:
                return False
            elif right.index(i) != left.index(li.pop(-1)):
                return False
    return len(li) == 0


for _ in lis:
    print(is_matched(_))

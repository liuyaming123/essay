# -*- coding:utf-8 -*-
"""判断是否是回文字符串"""


def is_circle(st):
    if len(st) < 2:
        return True
    if st[0] != st[-1]:
        return False
    print(st)
    return is_circle(st[1:-1])


if __name__ == '__main__':
    print(is_circle('1233321'))
    print(is_circle('122321'))

# -*- coding:utf-8 -*-
"""进制转换"""
'''
2进制满2进1，7进制满7进1...


2828的七进制数为11150
2828 = 7**0 * 0 + 7**1 * 5 + 7**2 * 1 + 7**3 * 1 + 7**4 * 1
'''


# 十进制转其他进制
def main(num, xxx):
    """
    :param num: 一个十进制整数
    :param xxx: 要转换的进制数，正整数
    :return: 以字符串的形式返回转换后的结果
    """

    sss = ''
    while num > 0:
        x = num % xxx
        sss = str(x) + sss
        num //= xxx
    return sss


if __name__ == '__main__':
    print(main(2828, 2))



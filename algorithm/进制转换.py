# -*- coding:utf-8 -*-
"""进制转换"""

'''
2进制满2进1，7进制满7进1...

188的10进制数为188
188 = 10**0 * 8 + 10**1 * 8 + 10**2 * 1
2828的七进制数为11150
2828 = 7**0 * 0 + 7**1 * 5 + 7**2 * 1 + 7**3 * 1 + 7**4 * 1
'''


def ten_to_other(num, xxx):
    """
    十进制转其他进制
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
    print(ten_to_other(2828, 7))


def other_to_ten(sss, xxx):
    """
    其他进制转十进制
    :param sss: 其他进制数，type of str
    :param xxx: 具体几进制, int
    :return: 返回对应的十进制数, int
    """

    num = 0
    for s in range(len(sss)):
        num += xxx**s * int(sss[::-1][s])

    return num


if __name__ == '__main__':
    print(other_to_ten('11150', 7))

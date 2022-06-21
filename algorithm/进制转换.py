# -*- coding:utf-8 -*-
"""进制转换"""

'''
2进制满2进1，7进制满7进1...

188的10进制数为188
188 = 10**0 * 8 + 10**1 * 8 + 10**2 * 1
2828的七进制数为11150
2828 = 7**0 * 0 + 7**1 * 5 + 7**2 * 1 + 7**3 * 1 + 7**4 * 1
'''

'''十进制转二进制'''
def transfer_binary(d):
    sli = []
    while d > 0:
        remainder = d % 2
        sli.append(str(remainder))
        d = d // 2
    return ''.join(sli[::-1])



'''十进制转任意进制'''
def transfer_common(d, base):
    digits = '0123456789ABCDEF'  # digits随着需要增加
    sli = []
    while d > 0:
        remainder = d % base
        sli.append(digits[remainder])
        d = d // base
    return ''.join(sli[::-1])


'''用递归实现整数转任意进制'''
def to_str(n, base):
    digits = '0123456789ABCDEF'
    if n < base:
        return digits[n]
    else:
        return to_str(n // base, base) + digits[n % base]


if __name__ == '__main__':
    print(transfer_common(100000, 16))
    print(to_str(100000, 16))

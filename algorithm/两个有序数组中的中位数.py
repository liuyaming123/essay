# -*- coding:utf-8 -*-
"""求两个有序数组中的中位数"""

'''
注意点：/ 真除得到的结果为浮点数, int函数对于浮点数向下取整
'''


def main(nums1, nums2):
    li = sorted(nums1 + nums2)
    length_li = len(li)
    if length_li == 1:
        return li[0]

    if length_li % 2 == 0:
        return (li[int((length_li / 2))] + li[int((length_li / 2 - 1))]) / 2

    if length_li % 2 == 1:
        i = int((length_li - 1) / 2)
        return li[i]

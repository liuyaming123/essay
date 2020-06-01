# -*- coding:utf-8 -*-
"""快速排序"""
'''
算法描述：
1、在数列之中，选择一个元素作为”基准”（pivot），或者叫比较值。
2、数列中所有元素都和这个基准值进行比较，如果比基准值小就移到基准值的左边，如果比基准值大就移到基准值的右边
3、以基准值左右两边的子列作为新数列，不断重复第一步和第二步，直到所有子集只剩下一个元素为止。
'''


def qsort(li):
    if len(li) < 2:  # 递归终止的条件
        return li

    mid = li[len(li) // 2]  # 选择中间元素作为对比项
    left, right = [], []  # 初始化左右列表

    li.remove(mid)  # 删除中间元素

    for i in li:
        if i < mid:
            left.append(i)
        else:
            right.append(i)

    return qsort(left) + [mid] + qsort(right)


# print(qsort([11, 99, 33, 69, 77, 88, 55, 11, 33, 36, 39, 66, 44, 22]))
print(qsort([2, 5, 1, 4, 3]))

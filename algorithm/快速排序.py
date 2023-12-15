# -*- coding:utf-8 -*-
"""快速排序"""
'''
算法描述：
1、在数列之中，选择一个元素作为”基准”（pivot），或者叫比较值。
2、数列中所有元素都和这个基准值进行比较，如果比基准值小就移到基准值的左边，如果比基准值大就移到基准值的右边
3、以基准值左右两边的子列作为新数列，不断重复第一步和第二步，直到所有子集只剩下一个元素为止。
'''


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    basis = arr[len(arr) // 2]  # 选择基准元素

    left = [i for i in arr if i < basis]
    middle = [i for i in arr if i == basis]
    right = [i for i in arr if i > basis]

    return quick_sort(left) + middle + quick_sort(right)

l = [8, 3, 7, 2, 4, 9, 1, 3]

res = quick_sort(l)
print(res)

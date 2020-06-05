# -*- coding:utf-8 -*-
"""二分查找算法"""


def half_search(lis, value, start=None, end=None, flag=0):
    if flag == 0:
        start = start if start else 0
        end = end if end else len(lis)-1

    if start <= end:
        mid = (start + end) // 2
        print(start, end, mid)  # 打印查找过程
        if lis[mid] == value:
            return mid
        elif lis[mid] > value:
            return half_search(lis, value, start, mid-1, flag=1)
        else:
            return half_search(lis, value, mid+1, end, flag=1)
    else:
        return None


if __name__ == '__main__':
    li = list(range(10000))
    li.remove(0)
    print(half_search(li, 99))

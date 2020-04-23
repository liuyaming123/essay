# -*- coding:utf-8 -*-
"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成
"""

"""
示例 1:
给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。
"""


def main(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return 1

    len_nums = len(nums)

    # if len_num >= 2:
    #     while nums[0] == nums[1]:
    #         nums.remove(nums[0])

    # if len_num >= 3:
    #     while nums[1] == nums[2]:
    #         nums.remove(nums[1])
    # if len_num >= 4:
    #     while nums[2] == nums[3]:
    #         nums.remove(nums[2])

    n = 2
    while len_nums >= n:
        if nums[n - 2] == nums[n - 1]:
            nums.remove(nums[n - 2])
            len_nums -= 1
        else:
            n += 1

    print(len_nums, nums)
    return len_nums


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    main(nums)

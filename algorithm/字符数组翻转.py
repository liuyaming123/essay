# -*- coding:utf-8 -*-
"""翻转字符数组"""

def reverse_str(chars):
    if chars:
        size = len(chars)
        for i in range(size // 2):
            chars[i], chars[size - 1 - i] = chars[size - 1 - i], chars[i]

    return chars

print(reverse_str(list("12345")))

# -*- coding:utf-8 -*-
"""求一个字符串的 无重复字符的最长字串的长度"""


def main(input_str):
    li = []
    ss = ''
    for i in input_str:
        if i not in ss:
            ss += i
        else:
            if ss not in li:
                li.append(ss)  # 如果重复，就把上一个未重复的子串添加到列表
            ss = li[-1].split(i)[-1]  # 用当前循环到的单个字符i去分割前一个添加到列表的子串，目的在于判断前一个添加到列表的子串是否包含当前字符i
            ss += i  # 上一行的结果一定不包含i
    li.append(ss)

    li.sort(key=lambda x: len(x))
    print(li)
    print(len(li[-1]))
    return len(li[-1])


if __name__ == '__main__':
    main('dvvdf')

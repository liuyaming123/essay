import numpy as np

# l1 = 'helloworldnnart'
# l2 = 'worldccarthe'
l1 = 'helloworldnnartsorrybeddkdkautifulmountnicesincerelyrldnnartsorrybeautifulmountgdhghfghghrttjyjghnfgnfgn'
l2 = 'worldccarthesinsidfgdnsincerelysorrbeautifulrldnndddartsorrybeautifulmoundghfghghghghdrttthjytt'

# 初始化一个len(l1)+1行，len(l2)+1列的布尔值矩阵，作为辅助理解
arr = np.zeros((len(l1) + 1, len(l2) + 1), dtype=int)

# 所有的连续的共有的子串都在 y = -x + b 的直线上，b可认为是直线的代表，范围为-len(l1) 到 len(l2),
bs = tuple(range(-len(l1), len(l2) + 1))
print(f'所有的线的b值--> {bs}')
# x = j, y = -i, 因为 y = -x + b => b = x + y，得 b = j - i
lines = {b: [{'boxs': [], 'length': 0}] for b in bs}

# # 两层for-loop
for i, ei in enumerate(l1, start=0):
    for j, ej in enumerate(l2, start=0):
        if ei == ej:
            arr[i][j] = 1
            index = j - i  # 代表线
            last = lines[index][-1]  # 每条线最后一个连续字符串对象
            if len(last['boxs']) == 0 or last['boxs'][-1] == (i - 1, j - 1):
                last['boxs'].append((i, j))
                last['length'] += 1
            elif len(last['boxs']) > 0 and last['boxs'][-1] != (i - 1, j - 1):
                lines[index].append({'boxs': [(i, j)], 'length': 1})

print(arr)
# print(lines)


length = 0
boxs = []
for b in lines:
    for i in lines[b]:
        if i['length'] > length:
            length = i['length']
            boxs = i['boxs']
            print(length, boxs)
# print(length, boxs)
print(f'两个字符串的最长公共子串为：{l1[boxs[0][0]:boxs[-1][0] + 1]}')

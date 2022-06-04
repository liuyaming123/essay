l = [1, 2, [3, 4], 5, [6, 7,{71,72,73}, 8, [(11, 22, 33)]], [55, 66, 77, [12, 34, 56], 78]]
res = []


def spread(li):
    for i in li:
        if '__len__' in dir(i):
            spread(i)
        else:
            res.append(i)


spread(l)
print(res)

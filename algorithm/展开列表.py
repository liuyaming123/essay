l = [1, 2, [3, 4], 5, [6, 7,'jdjk', 8, [(11, 22, 33)]], [55, 66, 77, [34, 56], 78]]
res = []


def spread(li):
    for i in li:
        if '__len__' in dir(i) and len(i) > 1:
            spread(i)
        else:
            res.append(i)


spread(l)
print(res)

# -*- coding:utf-8 -*-


try:
    r = 1 / 0
except:
    print('error')
else:
    print('else')
finally:
    print('finally\n')


for i in range(10):
    print(i)
    if i == 5:
        print()
        break
else:
    print('for循环执行完毕\n')


def f():
    try:
        r = 1 / 1
    except:
        print('error')
        return
    else:
        print('else')
        return
    finally:
        print('finally')

if __name__ == '__main__':
    f()
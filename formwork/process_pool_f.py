# -*- coding:utf-8 -*-

from concurrent.futures import ProcessPoolExecutor


def count(x: int):
    tot = 0
    for i in range(1, x+1):
        tot += i
    print(tot)
    return tot


def main():
    executor = ProcessPoolExecutor(max_workers=20)

    nums = [10**8 for _ in range(20)]
    for n in nums:
        executor.submit(count, n)
    executor.shutdown()
    print('work done!')


if __name__ == '__main__':
    main()

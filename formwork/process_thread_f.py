# -*- coding:utf-8 -*-
# 多进程多线程测试
# 进程池线程池测试

import time
import traceback
import requests
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

requests.packages.urllib3.disable_warnings()  # 取消警告


def get_ids():
    classify_ids = ['1', '2', '3', '4', '5', '6', ]
    cd_ids = []
    cnt = 0
    for cid in classify_ids:
        try:
            url = 'https://mnapi.tm51.com/h5/doings/doings?' \
                  'classify_id=%s&page=1&page_size=1000&sign=7bb2b50c76c7707eda4c78b45b9d6563c1c7f9c9' % cid
            res = requests.get(url, verify=False).json()
            print('total is %s' % res.get('data').get('total'))
            items = res.get('data').get('items')
            # pprint(items)
            for item in items:
                classify_id = item.get('classify_id')
                doings_id = item.get('doings_id')
                cd_ids.append((classify_id, doings_id))
                cnt += 1
            # time.sleep(1)
        except Exception as e:
            traceback.print_exc(e)
    print("items: %s" % cnt)
    return cd_ids


def get_data(ids):
    print(ids)
    try:
        classify_id, doings_id = ids[0], ids[1]
        url = 'https://mnapi.tm51.com/h5/doings/contents?' \
              'classify_id=%s&doings_id=%s&sign=72d2100da09f17e6a738ef704c8242d6ece808a2' \
              % (classify_id, doings_id)
        res = requests.get(url, verify=False, timeout=10)
        if res.status_code == 200:
            data = res.json()
            data = data.get('data')[0]
            print(data)

    except:
        traceback.print_exc()


# 时间装饰器
def times(x):
    print('time is start')
    start = time.time()
    x()
    end = time.time()
    used_time = end - start
    print('time is end', '\nstart time:%s' % start, '\nsend time:%s' % end, '\nused time %s' % used_time)
    return lambda: None


cd_ids = get_ids()


# @times
# def main():
#     p = multiprocessing.Pool(30)
#
#     for ids in cd_ids:
#         try:
#             p.apply_async(func=get_data, args=(ids,))
#         except:
#             pass
#     p.close()
#     p.join()
#     print('work done!')


# 线程池
# @times
# def main():
#     executor = ThreadPoolExecutor(max_workers=30)
#
#     for ids in cd_ids:
#         executor.submit(get_data, ids)
#     executor.shutdown(True)
#     print('work done!')


# 进程池
@times
def main():
    executor = ProcessPoolExecutor(max_workers=50)

    for ids in cd_ids:
        executor.submit(get_data, ids)
    executor.shutdown(True)
    print('work done!')


if __name__ == '__main__':
    main()

# -*- coding:utf-8 -*-


import csv

# 1. 创建文件对象
with open('文件名.csv', 'w', encoding='utf-8') as f:

    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)

    # 3. 构建列表头
    csv_writer.writerow(["姓名", "年龄", "性别"])

    # 4. 写入csv文件内容
    csv_writer.writerow(["l", '18', '男'])
    csv_writer.writerow(["c", '20', '男'])
    csv_writer.writerow(["w", '22', '女'])





# 将字典数据写入
# from pymongo import MongoClient
#
# test_conn = MongoClient("mongodb://10.16.20.228:25017")
# app_test = test_conn.apps.tou_test
#
#
# # 创建文件对象
# with open('hos.csv', 'w', encoding='utf-8') as f:
#     csv_writer = csv.writer(f)
#
#     for i in app_test.find():
#         data = i.get('data').get('hospital')
#         print(list(data.keys()))
#         print(list(data.values()))
#
#         csv_writer.writerow(list(data.keys()))
#         csv_writer.writerow(list(data.values()))
#         break
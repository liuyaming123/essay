# -*-coding:utf-8-*-
# 行列数据写入Excel

from pymongo import MongoClient
from pandas import DataFrame, read_excel

# user_conn = MongoClient("mongodb://10.16.20.228:25017")
# users = user_conn.users.users
#
# user_id, user_name, user_ip, user_topics \
#     = [], [], [], []
# for u in users.find().skip(100).limit(1000):
#     print(u)
#     id = u.get("_id")
#     name = u.get("user_name")
#     ip = u.get("ip")
#     topics = u.get("topics")
#
#     user_id.append(id)
#     user_name.append(name)
#     user_ip.append(ip)
#     user_topics.append(topics)
#
# data = {
#     'user_id': user_id,
#     'user_name': user_name,
#     'user_ip': user_ip,
#     'user_topics': user_topics,
# }
# df = DataFrame(data)
# df.to_excel('new.xls', startrow=1, index=False)


data = {
    'age': [11, 12, 13],
    'sex': ['男', '女', '男'],
    'name': ['张三', '李四', '王五'],
}

df = DataFrame(data)

# 存Excel
# df.to_excel('df_to.xls', startrow=1, index=False)

# 存html
# df.to_html('df_to.html', index=True, encoding='gbk')

# 存csv
# df.to_csv('df_to.csv')


# 读取文件
# res = read_excel('/Users/liu/practice/abc_play/formwork/new1.xls', header=0)
# print(res)

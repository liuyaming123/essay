# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch
es = Elasticsearch()


# 单条导入
data = {}  # 可以直接为json数据
es.index(index='test', body=data)


# 批量导入
# 在创建索引的同时设置settings和mappings后，进行批量导入
doc_index = "many_insert"
# doc_type = "_doc"  # 7.x不用设置，默认_type为_doc

doc_body = [

    {"index": {}},  # 可以不指定_id, 会自动生成_id

    {'name': 'jackaaa', 'age': 2000, 'sex': 1, 'address': '北京'},

    {"index": {"_id": 1}},  # 指定_id,默认_id为字符串类型，可以转成int类型在_source字段中

    {'name': 'jackbbb', 'age': 3000, 'sex': 2, 'address': '上海'},

    {"index": {}},

    {'name': 'jackccc', 'age': 4000, 'sex': 2, 'address': '广州'},

    {"index": {}},

    {'name': 'jackddd', 'age': 1000, 'sex': 1, 'address': '深圳'}

]


res = es.bulk(index=doc_index, body=doc_body, request_timeout=100)
print(res)

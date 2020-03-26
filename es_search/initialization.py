# -*- coding:utf-8 -*-
'''
initialization   美：[ɪˌnɪʃələˈzeɪʃn]
es-version: 7.6.1
'''

from pprint import pprint
from elasticsearch import Elasticsearch


# elasticsearch默认开启两个端口：9200，用于ES节点和外部通讯；9300，用于ES节点之间通讯
es = Elasticsearch('http://localhost:9200/'.split(','))


# 查询所有index名称
result = es.indices.get_alias().keys()
print(list(result))

# 查看指定index的mapping信息
# result = es.indices.get_mapping('people')
# pprint(result)

# 查看指定index的settings信息
# result = es.indices.get_settings('people')
# pprint(result)


# ================================================================================================
# ************************************************************************************************

# 7.x版本默认type为_doc,无需设置
# 一次性设置指定索引的分片、副本、类型
own_sm = {
    "settings": {
        "number_of_shards": 2,
        "number_of_replicas": 1
    },
    "mappings": {
        "properties": {
            "id": {"type": "long"},
            "name": {"type": "text"},
            "date": {"type": "date"},
            "text": {"type": "text", "analyzer": "standard"}
        }
    }
}


# 创建索引
own_index = 'test'
if not es.indices.exists(own_index):
    res = es.indices.create(own_index, body=own_sm)
    print(res)


# ================================================================================================
# ************************************************************************************************

# 动态设置
own_settings = {
    "settings": {
        # "number_of_shards": 3,  # 分片不能动态设置
        "number_of_replicas": 1  # 副本可以随时设置
    }
}

# mappings 已经创建mapping的字段不能改变，可以动态地添加未创建mapping的字段
own_mappings = {
    "properties": {
        # "id": {"type": "short"},
        # "name": {"type": "text"},
        "age": {"type": "short"}
    }
}

# res = es.indices.put_settings(index=own_index, body=own_settings)
# res = es.indices.put_mapping(index=own_index, body=own_mappings)
# print(res)

# ================================================================================================
# ************************************************************************************************

# 删除索引
# res = es.indices.delete('many_insert')
# print(res)

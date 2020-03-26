# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch
es = Elasticsearch()

'''
文档说明：
delete：删除指定index、id的文档
delete_by_query：删除满足条件的所有数据，查询条件必须符合DLS格式
'''


# 单一删除操作
# doc_index = "many_insert"
# # doc_type = "typeName"
# doc_id = "IdIZ3HABN9wJP77ho7Vu"

# res = es.delete(index=doc_index, id=doc_id)
# print(res)


# 批量删除操作
doc_index = "many_insert"
# doc_type = "typeName"

# 查询sex=1文档
doc_body_query = \
    {
        "query": {
            "bool": {
                "filter": {
                    "term": {
                        "sex": 1
                    }
                }
            }
        }
    }

# res = es.delete_by_query(index=doc_index, body=doc_body_query)
# print(res)


# 根据指定id批量删除
doc_body = [

    {"delete": {"_id": "MdJ83nABN9wJP77hIrWl"}},  # 只能根据指定_id批量删除

    {"delete": {"_id": 1}},  # 此方式不能指定其他字段删除

    {"delete": {"_id": "M9J83nABN9wJP77hIrWl"}},

]

res = es.bulk(index=doc_index, body=doc_body, request_timeout=100)
print(res)



'''
bulk接口说明：
在用bulk在批量操作的时候，对于不同的操作类型，一定要与之对应一个操作头信息（eg：{“index”: {}}， {‘delete’: {…}}， …），否则会报TransportError（400, u’illegal_argument_exception’）的错误。

---

#参考文档

>[https://blog.csdn.net/YHYR_YCY/article/details/78882011](https://blog.csdn.net/YHYR_YCY/article/details/78882011)

>[https://github.com/YHYR/ElasticSearchUtils/blob/master/utils/elasticsearchUtil.py](https://github.com/YHYR/ElasticSearchUtils/blob/master/utils/elasticsearchUtil.py)

>[https://blog.csdn.net/yhyr_ycy/article/details/78876391](https://blog.csdn.net/yhyr_ycy/article/details/78876391)
'''

# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch
es = Elasticsearch()

'''
文档说明：
update：跟新指定index、id所对应的文档
update_by_query：更新满足条件的所有数据，查询条件必须符合DLS格式
'''


'''单一操作'''
# doc_index = "many_insert"
# doc_id = "1"

# # 删除age字段
# doc_body = {
#     'script': "ctx._source.remove('address')"
# }

# # 修改或增加字段
# doc_body = {
#     "doc": {"name": 'jackaaa', "status": 1, }
# }

# res = es.update(index=doc_index, id=doc_id, body=doc_body)
# print(res)

# ================================================================================================


'''条件批量操作'''
doc_index = "many_insert"

# # 对所有文档,删除address字段
# doc_body_query = {
#     'query': {'match_all': {}},
#
#     'script': "ctx._source.remove('address')"
# }

# # 对所有文档,增加地址字段
# doc_body_query = {
#     'query': {'match_all': {}},
#
#     'script': "ctx._source.address = '合肥'"
# }

# 对所有文档, 修改名字字段
doc_body_query = {
    "query": {"bool": {"filter": [{"term": {"status": 1}}]}},

    "script": {
                "lang": "painless",
                "inline": "ctx._source.age = params.tag",
                "params": {
                    "tag": 19
                }
            }
}


res = es.update_by_query(index=doc_index, body=doc_body_query, request_timeout=100)
print(res)

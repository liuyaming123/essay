# -*- coding:utf-8 -*-


# 如果要在后台运行，使用./bin/elasticsearch -d启动
'''
bin/elasticsearch
bin/kibana
'''


# 集群启动命令
'''
bin/elasticsearch -E node.name=node0 -E cluster.name=geektime -E path.data=node0_data -d
bin/elasticsearch -E node.name=node1 -E cluster.name=geektime -E path.data=node1_data -d
bin/elasticsearch -E node.name=node2 -E cluster.name=geektime -E path.data=node2_data -d
bin/elasticsearch -E node.name=node3 -E cluster.name=geektime -E path.data=node3_data -d
'''


# 插件安装、删除
'''
bin/elasticsearch-plugin install xxx
bin/elasticsearch-plugin remove xxx
'''
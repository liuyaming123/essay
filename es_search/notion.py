# -*- coding:utf-8 -*-
'''
# notion  美 [ˈnoʊʃn]  观念;信念;理解
# conception  美 [kənˈsepʃn]  构思;构想;设想;理解(认为某事怎样或应该怎样);怀孕;受孕
'''


'''
shard = hash(routing) % number_of_primary_shards
routing 是一个可变值，默认是文档的 _id ，也可以设置成一个自定义的值。 
routing 通过 hash 函数生成一个数字，然后这个数字再除以 number_of_primary_shards （主分片的数量）后得到 余数 。
这个分布在 0 到 number_of_primary_shards-1 之间的余数，就是我们所寻求的文档所在分片的位置。
这就解释了为什么我们要在创建索引的时候就确定好主分片的数量 并且永远不会改变这个数量：因为如果数量变化了，那么所有之前路由的值都会无效，文档也再也找不到了。
'''

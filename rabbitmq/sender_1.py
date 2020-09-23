# -*- coding:utf-8 -*-

import pika
import json

credentials = pika.PlainCredentials('lym', '123456')  # mq用户名和密码
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               port=5672,
                                                               virtual_host='/',
                                                               credentials=credentials))

channel = connection.channel()  # 在socket基础上建立了rabbbitmq协议的通道

# 声明消息队列，消息将在这个队列传递，如不存在，则创建
channel.queue_declare(queue='order_ids')

# RabbitMQ a message can never be sent diirectly to the queue,
# it always needs to go though an exchange.

for i in range(10):
    message = json.dumps({'order_id': "%s" % i})
    # 向队列插入数值 routing_key是队列名
    channel.basic_publish(exchange='',
                          routing_key='order_ids',
                          body=message)
    print(message)


connection.close()



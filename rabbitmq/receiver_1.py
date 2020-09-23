# -*- coding:utf-8 -*-

import pika

credentials = pika.PlainCredentials('lym', '123456')  # mq用户名和密码
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               port=5672,
                                                               virtual_host='/',
                                                               credentials=credentials))

channel = connection.channel()  # 在socket基础上建立了rabbbitmq协议的通道

# 申明消息队列，消息在这个队列传递，如果不存在，则创建队列
channel.queue_declare(queue='order_ids', durable=False)


# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())


# 告诉rabbitmq，用callback来接收消息
channel.basic_consume('order_ids', callback)


# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
channel.start_consuming()

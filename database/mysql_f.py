# -*- coding:utf-8 -*-

import pymysql
import random
import time


class OperateMysql(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',
                                    port=3306,
                                    user='root',
                                    passwd='h1219932202',
                                    db='test',
                                    charset='utf8')  # 有中文的话加上charset，防止中文乱码

    def query(self, sql, rows=10):
        with self.conn.cursor() as cur:
            try:
                cur.execute(sql)
                result = cur.fetchmany(rows)
                return result
            except Exception as e:
                print(e)
                self.conn.rollback()

    def sql_exec(self, sql):
        with self.conn.cursor() as cur:
            try:
                cur.execute(sql)
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()

    def insert_many(self, sql, values_lis):  # values_lis: tuple of list
        with self.conn.cursor() as cur:
            try:
                cur.executemany(sql, values_lis)
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()


if __name__ == '__main__':
    '''创建操作对象'''
    OM = OperateMysql()
    # 查询
    res = OM.query('select id,name from people limit 2,4', )  # tuple of tuple
    print(res)

    '''新增或修改或删除'''
    # OM.sql_exec('insert into people(name,age,salary) values("%s",%s,%s)' % ('fish', 9, 15000))
    # OM.insert_or_ud('delete from people where id > 10000')

    '''批量新增'''
    # alphas = 'liuyaming'
    # values_lis = []
    # for i in range(1, 10001):
    #     item = (i, alphas[random.randint(0, 4):random.randint(5, 9)], i, i*100)
    #     values_lis.append(item)
    #
    # # 插入时如发现主键已存在，则替换原记录，即先删除原记录，后insert新记录
    # OM.insert_many('replace into people(id, name, age, salary) values(%s, %s, %s, %s)', values_lis)

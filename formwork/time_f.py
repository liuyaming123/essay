# -*- coding:utf-8 -*-

import datetime
import time


# 获取现在的时间
a = datetime.datetime.now()
# print(a.__format__("%Y-%m-%d %H:%M:%S"))  # 与此方法等价的方法为strftime(...)
# print(a.strftime("%M"))

# 仅获取今天年月日
b = datetime.date.today()
# print(b)
# print(type(b))

# 拿今天的年，月，日
c = (datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
# print(c)


# 计算时间差，可以计算: 天(days), 小时(hours), 分钟(minutes), 秒(seconds), 微秒(microseconds).
d1 = datetime.datetime.now()
# d2 = d1 + datetime.timedelta(hours=8)
# d2 = d1 - datetime.timedelta(days=2)
# d2 = d2.strftime("%Y-%m-%d")
# print(d2)
# print(type(d2))



def get_changed_date(change, format_, sources_time=None):
    """
    Change and to string
    :param sources_time: sources time, if sources time is None then sources time = now
    :param change: time = now + change
    :param format_: result time format
    :return:
    """
    if sources_time is None:
        now = time.time()
    else:
        now = sources_time
    change_time = now + change
    change_time = time.localtime(change_time)
    str_time = time.strftime(format_, change_time)
    return "%s" % str_time


def get_changed_time(change, format_, sources_time=None):
    """
    Change and to timestamp
    :param sources_time: sources time, if sources time is None then sources time = now
    :param change: time = now + change
    :param format_: result time format
    :return:
    """
    time_str = get_changed_date(change, format_, sources_time)
    ti = time.mktime(time.strptime(time_str, format_))
    return ti




# pre_3_days = int(get_changed_time(- 3 * 24 * 60 * 60, "%Y%m%d %H%M%S"))
# pre_3_days = int(get_changed_time(- 3 * 24 * 60 * 60, "%Y%m%d %H%M%S"))
pre_3_days = int(get_changed_time(- 3 * 24 * 60 * 60, "%Y%m%d %H%M%S"))
# print(pre_3_days)


def get_pre_time(pre_day=0):
    """获取几天前或几天后的时间戳，当前时间之前为负，之后为正"""
    pre_day_timestamp = int(get_changed_time(pre_day * 24 * 60 * 60, "%Y%m%d %H%M%S"))
    return pre_day_timestamp


print(get_pre_time(-15))


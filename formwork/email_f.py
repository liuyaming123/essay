# -*- coding:utf-8 -*-
"""邮件发送"""

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


"""设置发送方信息"""
# ================================
# smtp服务地址
host = 'smtp.163.com'
# 端口
port = 465
# 发件人
user = 'lym_6017@163.com'
# 授权码
pwd = 'VYASAYBPGIZPJFRK'
# ================================


class SendEMail(object):
    """封装发送邮件类"""

    def __init__(self):
        # 第一步：连接到smtp服务器
        self.smtp_s = smtplib.SMTP_SSL(host=host,
                                       port=port)
        # 第二步：登陆smtp服务器
        self.smtp_s.login(user=user,
                          password=pwd)

    def send_text(self, to_user, content, subject):
        """
        发送文本邮件
        :param to_user: 对方邮箱
        :param content: 邮件正文
        :param subject: 邮件主题
        :return:
        """
        # 第三步：准备邮件
        # 使用email构造邮件
        msg = MIMEText(content, _subtype='plain', _charset="utf8")
        # 添加发件人
        msg["From"] = user
        # 添加收件人
        msg["To"] = to_user
        # 添加邮件主题
        msg["subject"] = subject
        # 第四步：发送邮件
        self.smtp_s.send_message(msg, from_addr=user, to_addrs=to_user)

    def send_file(self, to_user, content, subject, reports_path, file_name):
        """
        发送测试报告邮件
        :param to_user: 对方邮箱
        :param content: 邮件正文
        :param subject: 邮件主题
        :param reports_path: 测试报告路径
        :param file_name: 发送时测试报告名称
        """
        # 读取报告文件中的内容
        file_content = open(reports_path, "rb").read()
        # 2.使用email构造邮件
        # （1）构造一封多组件的邮件
        msg = MIMEMultipart()
        # (2)往多组件邮件中加入文本内容
        text_msg = MIMEText(content, _subtype='plain', _charset="utf8")
        msg.attach(text_msg)
        # (3)往多组件邮件中加入文件附件
        file_msg = MIMEApplication(file_content)
        file_msg.add_header('content-disposition', 'attachment', filename=file_name)
        msg.attach(file_msg)
        # 添加发件人
        msg["From"] = user
        # 添加收件人
        msg["To"] = to_user
        # 添加邮件主题
        msg["subject"] = subject
        # 第四步：发送邮件
        self.smtp_s.send_message(msg, from_addr=user, to_addrs=to_user)


if __name__ == '__main__':

    """测试发送文本"""
    # --------------------------------------------------------------------
    # # 收件人
    # to_user = '1219932202@qq.com'
    # # 邮件正文
    # content = '这是一个多么好的夜晚！But you use it to watch "还珠格格"'
    # # 邮件主题
    # subject = '批评'
    #
    # SE = SendEMail()
    # SE.send_text(to_user, content, subject)
    # --------------------------------------------------------------------

    """测试发送文本及附件"""
    # --------------------------------------------------------------------
    # 收件人
    to_user = '739710328@qq.com'
    # 邮件正文
    content = '这是一个附件'
    # 邮件主题
    subject = '这是主题'

    reports_path = '/Users/liu/practice/abc_play/play/hos.csv'
    # file_name = 'hos.csv'  # 发送附件的名称（可自定义）
    file_name = 'haha.csv'

    SE = SendEMail()
    SE.send_file(to_user, content, subject, reports_path, file_name)
    # --------------------------------------------------------------------

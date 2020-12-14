import models  # 导入对应的models
import requests

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
# 初始化数据库连接:
on_line_database = ''
on_test_database = ''
engine = create_engine(on_line_database)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(models.User).filter(models.User.id=='5').one()
print(user.name)

session.close()



# test_host = 'http://39.100.106.9:8000'
#
# prod_host = 'http://recruit.cyclone-robotics.com'
#
#
#
# def send_interview_feedback_notification():
#     # 创建session
#     session = DBSession()
#
#
#     for interview in session.query(models.Interview).filter(
#         models.Interview.status.is_(None),
#     ).all():  # type: models.Interview
#
#         interviewer: models.User = session.query(models.User).filter(models.User.id == interview.interviewer_id).first()
#         try:
#             user_info = fss.get_user_info_by_mobile(interviewer.phone)
#         except Exception as e:
#             print(e)
#             continue
#         candidate: models.Candidate = session.query(models.Candidate).filter(models.Candidate.id == interview.candidate_id).first()
#         position: models.Position = session.query(models.Position).filter(models.Position.id == candidate.position_id).first()
#
#         print(interview.id, interviewer.name, interviewer.phone, candidate.name, position.position_name)
#
#     # 关闭session
#     session.close()
#
#
# if __name__ == '__main__':
#     send_interview_feedback_notification()


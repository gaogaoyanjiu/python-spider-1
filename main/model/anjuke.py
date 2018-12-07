#-*-coding:utf-8-*-
'''租房信息模板类'''
from sqlalchemy import Column, String, Integer
from main.util.dbutil import *

class anjuke_house(Base):
    # 表名
    __tablename__ = 'anjuke'

    # 主键
    id = Column(String(32), default=gen_id, primary_key=True)
    # 房屋描述
    detail = Column(String(48))
    # 房屋户型
    house_type = Column(String(20))
    # 每月租金
    price = Column(Integer)
    # 所在小区
    village = Column(String(48))
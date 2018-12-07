#-*-coding:utf-8-*-
'''数据库工具类'''
import uuid
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from main.util import config

# 初始化引擎
engine = create_engine('mysql+mysqlconnector://%(username)s:%(password)s@%(ip)s:%(port)s/%(dbname)s' % config.db, echo=True)
# 创建Session工厂
SessionFactory = sessionmaker(bind=engine)

# 获取连接
def get_session():
    return scoped_session(SessionFactory)

# 创建orm模板基类
Base = declarative_base()

# 创建表格
def create_table():
    Base.metadata.create_all(engine)

# 添加一条数据
def save(data):
    try:
        session = get_session()
        session.add(data)
        session.commit()
    finally:
        session.remove()    #将连接放回连接池

# 执行原生sql语句
def execute_sql(sql):
    try:
        session = get_session()
        return session.execute(sql)
    finally:
        session.remove()

# 生成uuid
def gen_id():
    uid = str(uuid.uuid1())
    return ''.join(uid.split('-'))
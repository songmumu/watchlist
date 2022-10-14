from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer

# create_engine('数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名') 用来初始化数据库连接
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/anyuci')
# 创建对象的基类
Base = declarative_base()
# 创建 DBSession 类型
DBSession = sessionmaker(bind=engine)


class User(Base):
    # __tablename__ 指定在 MySQL 中表的名字
    __tablename__ = 'Users'
    # Column 定义数据库中表的结构
    id = Column(Integer, primary_key=True)
    nickname = Column(String(64), nullable=False, index=True)
    phone = Column(Integer, unique=True, nullable=False, index=True)
    password = Column(String(64), nullable=False)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


# 创建数据表
if __name__ == '__main__':
    Base.metadata.create_all(engine)

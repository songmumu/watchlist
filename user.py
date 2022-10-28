from database import DBSession, User

# 创建 session 对象
session = DBSession()


# 添加新用户
def add_user(nickname, openID, password):
    # 创建新 User 对象
    new_user = User(nickname=nickname, openID=openID, password=password)
    # 添加到 session
    session.add(new_user)
    # 提交并保存到数据库
    session.commit()
    # 关闭session
    session.close()

# 查询所有用户
def query_all_user():
    users = session.query(User).all()
    return users

# 查询第一个用户
def query_first_user():
    first_user = session.query(User).first()
    return first_user
from database import DBSession, User

# 创建 session 对象
session = DBSession()


# 添加新用户
def add_user(nickname, password, phone):
    # 创建新 User 对象
    new_user = User(nickname=nickname, password=password, phone=phone)
    # 添加到 session
    session.add(new_user)
    # 提交并保存到数据库
    session.commit()
    # 关闭session
    session.close()

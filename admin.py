from database import DBSession, Admin

# 创建 session 对象
session = DBSession()

# 添加管理员
def add_admin(username, password):
    # 创建新 User 对象
    new_admin = Admin(username=username, password=password)
    # 添加到 session
    session.add(new_admin)
    # 提交并保存到数据库
    session.commit()
    # 关闭session
    session.close()

# 根据用户名查询管理员
def query_admin(username):
    return session.query(Admin).filter(Admin.username==username).first()
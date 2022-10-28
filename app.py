from flask import Flask, render_template, request, redirect, url_for
from markupsafe import escape
from flask_bootstrap import Bootstrap4
from user import add_user, query_all_user, query_first_user
from admin import add_admin, query_admin


app = Flask(__name__)

bootstrap = Bootstrap4(app)
if __name__ == '__main__':
    app.run()


"""
    小程序 api
"""

@app.route('/user/register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        openID = request.form.get('openID')
        password = request.form.get('password')
        add_user(nickname, openID, password)
        return {'msg': 'success'}, 200

@app.route('/user/login', methods=['POST'])
def user_login():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        login(nickname)


"""
后台管理系统 api
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/admin/to_register', methods=['GET', 'POST'])
def admin_to_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        add_admin(username, password)
        return {'msg': 'success'}, 200


@app.route('/admin/to_login', methods=['GET', 'POST'])
def admin_to_register():
    if request.method == 'POST':
        username = escape(request.form.get('username')).striptags()
        password = escape(request.form.get('password')).striptags()
        db_username = query_admin(username).username
        db_password = query_admin(username).password
        return {'msg': db_username ,'msg2': db_password }, 200





# 对于多个模板内都需要使用的变量，可以使用app.context_processor 装饰器注册一个模板上下文处理函数，这个函数返回的变量（以字典键值对的形式）将会统一注入到每一个模板的上下文环境中，因此可以在模板中直接使用
@app.context_processor
def inject_user():
    username= query_first_user().nickname
    return dict(username=username) #需要返回字典，等同于 return {'user', user}


# app.errorhandler()装饰器注册一个错误的处理函数，当发生404错误时，这个函数就会被触发
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



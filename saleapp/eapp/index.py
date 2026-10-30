import math
from flask import render_template, request, redirect
from saleapp.eapp import app, dao,login
from flask_login import login_user
from flask_login import logout_user

@app.route('/')
def index():
    count=dao.count_products()
    page_size=app.config['PAGE_SIZE']
    products=dao.load_products(kw=request.args.get('kw'),cate_id=request.args.get('category_id'), page=int(request.args.get('page',1)))
    return render_template('index.html', products=products, page=math.ceil(count/page_size))
@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/logout')
def logout_view():
    logout_user()
    return redirect('/login')

@app.route('/login', methods=['post'])
def login_process():
    username= request.form.get('username')
    password = request.form.get('password')

    u= dao.authorize(username,password)
    if u:
        login_user(user=u)

    return redirect('/') if request.args.get('from') else redirect('/admin')


@app.route('/register')
def register_view():
    return render_template('register.html')

@app.route('/register', methods=['post'])
def register_process():
    password=request.form.get('password')
    confirm=request.form.get('confirm')
    msg=''
    if not password or not confirm or password != confirm:
        msg='Mật khẩu không khớp'
    return render_template('register.html',msg=msg)

@app.context_processor
def common_responses():
    return {
        'categories': dao.load_category()
    }

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if (__name__) == '__main__':
    with app.app_context():
        from saleapp.eapp import admin
        app.run(debug=True)

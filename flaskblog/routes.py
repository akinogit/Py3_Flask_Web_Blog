from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db ,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import USER_INFO, Post
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author': 'SA',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '2020 01 05'
    },
    {
        'author': 'RM',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '2020 01 05'
    }
]

#Flaskでは@app.route()でルーティングを行う
@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html',posts=posts)

@app.route('/about')
def about():
  return render_template('about.html',title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = USER_INFO(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
        # 初期表示時
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # POSTリクエスト(ログイン時)
        user = USER_INFO.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            # 初期表示時
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
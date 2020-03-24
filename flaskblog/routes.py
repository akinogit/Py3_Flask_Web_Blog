from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import USER_INFO, Post


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


# ----- 追加 -----
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # POSTリクエスト(登録時)
        flash('Account created for %s!' % form.username.data, 'success')
        return redirect(url_for('home'))
        # 初期表示時
    return render_template('register.html', title='Register', form=form)


# ----- 追加 -----
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # POSTリクエスト(ログイン時)
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            # 初期表示時
    return render_template('login.html', title='Login', form=form)
"""
Top Page
@author Aki Suzuki
"""

#=====import
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flaskblog.forms import RegistrationForm, LoginForm
#=====import EOF
app = Flask(__name__)
app.config.from_object('instance.config')
app.config.from_object('instance.postgresql')
#app.config['SECRET_KEY'] = '311a2873aeb05edd55fd2ff4b0b605d1'
db = SQLAlchemy(app)

class USER_INFO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User('{}', '{}', '{}')".format(self.username, self.email, self.image_file)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "Post('{}', '{}')".format(self.title, self.date_posted)

#=====html template
# home.htmlに渡すデータ
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
#=====html template EOF
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

#pythonファイルを直に指定してWebサーバを起動させるための宣言
if __name__ == '__main__':
 app.run(debug=True)

#===== EOF =====
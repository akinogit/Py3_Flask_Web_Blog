from datetime import datetime
from flaskblog import db ,login_manager
from flask_login import UserMixin


# ---- 追加 ----
@login_manager.user_loader
def load_user(user_id):
    return USER_INFO.query.get(int(user_id))

class USER_INFO(db.Model,UserMixin):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
#    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return 'USER_INFO(username={0},email={1},image_file{2})'.format(self.username, self.email, self.image_file)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "Post('{}', '{}')".format(self.title, self.date_posted)
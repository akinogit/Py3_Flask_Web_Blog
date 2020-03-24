from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('instance.config')
app.config.from_object('instance.postgresql')
#app.config['SECRET_KEY'] = '311a2873aeb05edd55fd2ff4b0b605d1'
db = SQLAlchemy(app)

from flaskblog import routes
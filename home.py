"""
Top Page
@author Aki Suzuki
"""

#=====import
from flask import Flask ,render_template
#=====import EOF
app = Flask(__name__)
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

#pythonファイルを直に指定してWebサーバを起動させるための宣言
if __name__ == '__main__':
 app.run(debug=True)

#===== EOF =====
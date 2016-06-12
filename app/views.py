from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Roadhog'}
    posts = [
        {
            'author': {'nickname': 'McCree'},
            'body': 'It''s high noon!'
        },
        {
            'author': {'nickname': 'Reinhardt'},
            'body': 'Catch Phrase!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

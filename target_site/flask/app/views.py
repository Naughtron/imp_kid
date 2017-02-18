from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Naughtron'} # just some user
    # create array some fake posts
    posts = [
        {
        'author': {'nickname': 'Naughtron'},
        'body': 'You can\'t fax glitter!'
        },
        {
        'author': {'nickname': 'Some_Dude'},
        'body': 'well, not with that attitude!'
        }
    ]
    return render_template('index.html',
                           #title='Home',
                           user=user,
                           posts=posts)

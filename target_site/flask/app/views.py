from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

#@app.route('/')
#@app.route('/index')
@app.route('/login', methods=['GET', 'POST']) # if not spec only GET works

# def index():
#     user = {'nickname': 'Naughtron'} # just some user
#     # create array some fake posts
#     posts = [
#         {
#         'author': {'nickname': 'Naughtron'},
#         'body': 'You can\'t fax glitter!'
#         },
#         {
#         'author': {'nickname': 'Some_Dude'},
#         'body': 'well, not with that attitude!'
#         }
#     ]
#     return render_template('index.html',
#                            #title='Home',
#                            user=user,
#                            posts=posts)

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

from flask import render_template,redirect,url_for,request
from twittor.forms import Loginform
from twittor.models import User,Tweet
from flask_login import login_user,current_user,logout_user,login_required

@login_required
def index():
    name={'username':current_user.username}
    title='bark'
    posts=[
        {
            'author':{'username':'root'},
            'body':"hi i'm root"
        },
        {
            'author':{'username':'test'},
            'body':"hi i'm test"
        },
    ]
    return render_template('index.html',name=name,title=title,posts=posts)

def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=Loginform(meta={'csrf': False})
    if form.validate_on_submit():
        u=User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            print('Invalid username or password')
            return redirect(url_for('login'))
        login_user(u,remember=form.remember_me.data)
        next_page=request.args.get('next')
        if next_page:
            return redirect(url_for(next_page))
        return redirect(url_for('index'))
    return render_template('login.html',title="Sign In",form=form)
def logout():
    logout_user()
    return redirect(url_for('login'))
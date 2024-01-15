<<<<<<< HEAD
from flask import render_template,redirect,url_for
from twittor.forms import Loginform

def index():
    name={'username':'tester'}
    title='bark'
=======
from flask import render_template,redirect,url_for,request,abort
from twittor.forms import Loginform,Registerform,EditProfileform
from twittor.models import User,Tweet
from flask_login import login_user,current_user,logout_user,login_required
from twittor import db

@login_required
def index():
>>>>>>> 0.6
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
<<<<<<< HEAD
    return render_template('index.html',name=name,title=title,posts=posts)

def login():
    form=Loginform(meta={'csrf': False})
    if form.validate_on_submit():
        msg="username={},passwird={},remember_me={}".format(
        form.username.data,
        form.password.data,
        form.remember_me.data
        )
        print(msg)
        return redirect(url_for('index'))
    return render_template('login.html',title="Sign In",form=form)
=======
    return render_template('index.html',posts=posts)

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


def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=Registerform(meta={'csrf': False})
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',title="Register",form=form)

@login_required
def user(username):
    u=User.query.filter_by(username=username).first()
    if u is None:
        abort(404)
    posts=[
        {
            'author':{'username':u.username},
            'body':"hi i'm {}!".format(u.username)
        },
        {
            'author':{'username':u.username},
            'body':"hi i'm {}!".format(u.username)
        },
    ]
    return render_template('user.html',title='profile',posts=posts,user=u)

def page_not_found(e):
    return render_template('404.html'),404

@login_required
def edit_profile():
    form=EditProfileform()
    if request.method=='GET':
        form.about_me.data=current_user.about_me
    if request.method=='POST':
        current_user.about_me=form.about_me.data
        db.session.commit()
        return redirect(url_for('profile',username=current_user.username))
    return render_template('edit_profile.html',form=form)
>>>>>>> 0.6

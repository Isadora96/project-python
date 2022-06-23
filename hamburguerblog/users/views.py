from crypt import methods
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from hamburguerblog import db
from hamburguerblog.models import User, BlogPost
from hamburguerblog.users.forms import RegistrationForm,LoginForm,UpdateUserForm
from hamburguerblog.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)


# register
@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        
        db.session.add(user)
        db.session.commit()
        flash('Thanks form registration!')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)

# log in
@users.route("/login", methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

            if user.check_password(form.password.data) and user is not None:

                    login_user(user)
                    flash('Log in Sucess!')

                    #if user is trying to visit a page that require a log in

                    next = request.args.get('next')

                    #if user not requested any page or the page is not homepage 
                    if next == None or not next[0]=='/':
                        #next will be the homepage
                        next = url_for('core.index')
                    
                    #if next is post.html e.g, then go to this page
                    return redirect(next)

    return render_template('login.html', form=form)

# logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('core.index'))
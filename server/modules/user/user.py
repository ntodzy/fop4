from flask import Flask, Blueprint, render_template, request, session, redirect, url_for,current_app

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin, current_user,login_required, login_user, logout_user

from modules.user._user import LoginForm, SignupForm
from modules.user._user import User, db
userManagement = Blueprint('user', __name__)
loginManagement = Blueprint('login', __name__)

loginManager = LoginManager()

@loginManager.user_loader
def load_user(id):
  return User.query.get(int(id))

@userManagement.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return(redirect(url_for('admin_dashboard')))

  form = LoginForm()
  if form.validate_on_submit():
        username = request.form.get('username')
        user = User.query.filter_by(username=username).first()

        if user:
          if user.check_password(password=request.form.get('password')):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('admin_dashboard'))

  return(redirect(url_for('admin_dashboard')))


# @userManagement.route('/signup', methods=['GET', 'POST'])
# def auth_signup():
#   if current_user.is_authenticated:
#     return redirect(url_for('render_dashboardSite'))

#   form = SignupForm()
#   if form.validate_on_submit():
#         username = request.form.get('username')
#         password = request.form.get('password')
#         email = request.form.get('email')

#         user = User(username=username, email=email)
#         user.set_password(password)

#         db.session.add(user)
#         db.session.commit()
        
#         return redirect(url_for('user.login'))

  # return render_template('signup.html', title='Sign Up', form=form)

@userManagement.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_bp.route_index'))

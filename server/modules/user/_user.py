from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

import pickle

db = SQLAlchemy()

class User(db.Model, UserMixin):
  __tablename__ = 'flasklogin-users'

  id = db.Column(db.Integer, primary_key=True)

  username = db.Column(db.String(256), unique=True)

  email = db.Column(db.String(120), index=True)

  password_hash = db.Column(db.String(128))

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):

    return check_password_hash(self.password_hash, password)
  
  def __repr__(self):
    return '<User {}>'.format(self.username)
  
class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  submit = SubmitField('Sign Up')

from main import app

with app.app_context():
  db.create_all()
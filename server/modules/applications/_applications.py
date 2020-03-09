from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text
from modules.user._user import db
from main import app

class Applications(db.Model):
  __tablename__ = 'applications'
  
  id = db.Column(db.Integer, primary_key=True)

  _metadata = db.Column(db.PickleType)

  content = db.Column(db.PickleType)

  status = db.Column(db.Integer)

def getApplications(sfilter):
  data = None
  qstatus = str(sfilter)


  with app.app_context():
    try:

      data = db.session.query(Applications).filter_by(status=sfilter).all()

      print(data)
    except OperationalError as err:
      print(err)

  return data

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField, IntegerField

from wtforms.validators import DataRequired

class ApplicationForm(FlaskForm):
  first = StringField('First Name', validators=[DataRequired()])
  last = StringField('Last Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  sr = IntegerField('What is your skill rating in overwatch?', validators=[DataRequired()])

  computer = BooleanField('Do you have a computer that can run Overwatch?', validators=[DataRequired()])

  day_hours = StringField('How many hours on the weekday could you play?', validators=[DataRequired()])

  week_hours = SelectField('How many hours do you play each week', validators=[DataRequired()],
  choices=[("s", '0-4'),
    ("ms", "4-8"),
    ( "m","8-12"),
    ('ml',"12-16"),
    ( 'l',"16-24"),
    ('xl',"24+")])

  activities = StringField('What activities do you do outside of school/gaming? ')

  submit = SubmitField('Apply!')
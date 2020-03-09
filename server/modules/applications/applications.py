from flask import Flask, Blueprint, request, redirect, url_for, render_template
from modules.applications._applications import ApplicationForm, Applications
from modules.user._user import db, User
from datetime import datetime

applications = Blueprint('applications', __name__)

@applications.route('/apply', methods=['GET', 'POST'])
def apply():
  form = ApplicationForm()
  # First, Last, Email
  if form.validate_on_submit():
    first = request.form.get('first')
    last = request.form.get('last')
    email = request.form.get('email')

    metadata = {
      'name': {
        'first': first,
        'last': last
      },
      'email': email,
      'created-at': datetime.utcnow(),
      'updated-at': None
    }

    content = {
      'computer': request.form.get('computer'),
      'sr': request.form.get('sr'),
      'dhours': request.form.get('day_hours'),
      'week_hours': request.form.get('week_hours'),
      'activities': request.form.get('activities'),

    }

    application = Applications(_metadata=metadata, content=content,status="pending")

    db.session.add(application)
    db.session.commit()
        
    return redirect(url_for('user.login'))


  return render_template('apply.html', title='Apply Now!', form=form)

@applications.route('/tuser')
def tuser():
  user = User(username="app_review", email="appreview@oogabooga.com")
  user.set_password("mcd0na1dz!")

  db.session.add(user)
  db.session.commit()
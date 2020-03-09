from modules.user._user import User
from flask_login import login_user
from flask import request, jsonify
import json

from flask_mail import Message
from modules.mail.mail import mail

def is_login(arg1):
  username = arg1['username']
  user = User.query.filter_by(username=username).first()

  if user:

    if arg1['password'] == user.password_hash: # Because Flask can only grab hashed password when creating a accept/deny function in Flask we can also create a post request that bundles in the hashed password!

      login_user(user)
      return [True, "User has been logged in"]

    else:
      if user.check_password( password = arg1['password']):
        login_user(user)

        return[True,"User has been logged in!"]

      else:
        return [False,"Invalid Username or Password."]

  else:
    return [False,"Authorization Error"]

def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    # mail.send(msg) Enable if you really want to send emails. I cant be bothered to setup STMP on an email account so thats why this is blank.
    
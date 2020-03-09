from flask import Flask, Blueprint, jsonify, request, render_template
from flask_login import login_user
import json
from modules.applications._applications import getApplications, Applications
from modules.user._user import db, User
from modules.mail.mail import senders

from  api._util import is_login, send_email

api = Blueprint('api', __name__, url_prefix="/api")

@api.route('/get/applications')
def returnApplication():

  data = {}

  for i in getApplications(request.args.get('cmd')):
    data[i.id] = {
      'metadata': i._metadata,
      'content': i.content
     }

  return data

@api.route('/application', methods=['POST'])
def setApplication():
  _login = is_login(request.authorization)
  if _login[0] == True:
    
    print(request.data)
    
    data  = json.loads(request.data)
    
    application = Applications.query.get(data["id"])

    if data["status"] == "denied":

      application.status = "denied"
      send_email(
        "Application {} has been updated!".format(data["id"]),
        senders[0],
        application._metadata['email'],
        render_template('rejection.txt', data=data, application=application)
      )

      db.session.add(application)
      db.session.commit()
      
      return "Email has been sent! Applicant has been denied!" 
    
    else:
      if data["status"] == "approved": 
        application.status = "approved"


        send_email(
          "Application {} has been updated!".format(data["id"]),
          senders[0],
          application._metadata['email'],
          render_template('acception.txt', data=data, application=application)
        )

        db.session.add(application)
        db.session.commit()

        return "Email has been sent! Applicant has been accepted!"

  else:

    return _login[1]
from flask_mail import Mail
import os

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
# Ideally this would be filled out yet email support isn't very important yet the instances are still there to notifiy the user

# administrator list
senders = ['foo@bar.com']

mail = Mail()
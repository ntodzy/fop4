from flask import Flask

app = Flask(__name__)

# Database Garbage
from modules.user._user import db, User
db.init_app(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] =  'ap$ncu&ase#asmd$lasd%paqq^@asdx'

# Mail Garbage

from modules.mail.mail import mail
mail.init_app(app)

# User Garbage

from modules.user.user import userManagement, loginManagement, loginManager

app.register_blueprint(userManagement)
app.register_blueprint(loginManagement)

loginManager.init_app(app)
loginManager.login_view = 'user.login'



from modules.applications.applications import applications
app.register_blueprint(applications)

from api.api import api
app.register_blueprint(api)

@app.route('/')
def index():
  
  return "Index"


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
from flask_login import LoginManager
from flaskblog import app
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

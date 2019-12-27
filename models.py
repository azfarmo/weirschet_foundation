from datetime import datetime
from loginmanager import login_manager
from flask_login import UserMixin
from app import app

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(20),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    allergies = db.Column(db.Text, nullable=False)
    name = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    contact = db.Column(db.String(20))
    def __repr__(self):
        return f"Post('{self.id}', '{self.date_posted}')"
    
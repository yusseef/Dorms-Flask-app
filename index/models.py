from datetime import datetime
from index import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#singleton model


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    age = db.Column(db.String, nullable=False)
    city = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    faculty_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"Users('{self.username}', '{self.email}', '{self.image_file}', '{self.age}', '{self.city}'," \
               f" '{self.phone}', '{self.gender}', '{self.faculty_name}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    gender = db.Column(db.String(30), nullable=False)
    Faculty_name = db.Column(db.String(30), nullable=True)
    phone = db.Column(db.String(30), nullable=False)
    interest = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Posts('{self.title}', '{self.data_posted}', '{self.gender}', '{self.Faculty_name}', '{self.phone}'," \
               f" '{self.interest}', '{self.description}')"

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    date_joined   = db.Column(db.DateTime, default=datetime.utcnow)

    profiles    = db.relationship('Profile',   backref='user',    lazy=True)
    favourites  = db.relationship('Favourite', backref='requester', lazy=True)

    def set_password(self, pw):
        self.password_hash = generate_password_hash(pw)

    def check_password(self, pw):
        return check_password_hash(self.password_hash, pw)

class Profile(db.Model):
    __tablename__ = 'profiles'
    id                 = db.Column(db.Integer,  primary_key=True)
    user_id            = db.Column(db.Integer,  db.ForeignKey('users.id'), nullable=False)
    description        = db.Column(db.Text,     nullable=False)
    parish             = db.Column(db.String(50), nullable=False)
    biography          = db.Column(db.Text,     nullable=False)
    sex                = db.Column(db.String(10), nullable=False)
    race               = db.Column(db.String(20), nullable=False)
    birth_year         = db.Column(db.Integer,  nullable=False)
    height             = db.Column(db.Float,    nullable=False)
    fav_cuisine        = db.Column(db.String(50))
    fav_colour         = db.Column(db.String(20))
    fav_school_subject = db.Column(db.String(50))
    political          = db.Column(db.Boolean,  default=False)
    religious          = db.Column(db.Boolean,  default=False)
    family_oriented    = db.Column(db.Boolean,  default=False)

class Favourite(db.Model):
    __tablename__ = 'favourites'
    id          = db.Column(db.Integer,  primary_key=True)
    user_id     = db.Column(db.Integer,  db.ForeignKey('users.id'), nullable=False)
    fav_user_id = db.Column(db.Integer,  nullable=False)
    timestamp   = db.Column(db.DateTime, default=datetime.utcnow)